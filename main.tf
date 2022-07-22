provider "aws" {
    region = "us-east-1"

}

terraform {
  backend "s3" {
    bucket = "tfstate-pspy-eddsarg"
    key = "pspy.tfstate"
    region = "us-east-1"
    dynamodb_table = "tfstate-pspy-eddsarg"
  }
}

### Main VPC

resource "aws_vpc" "main" {
    cidr_block = "172.17.0.0/16"
    instance_tenancy = "default"

    tags = {
        Name = "pspyVPC-eddsarg"
    }
}

# Main Subnet
resource "aws_subnet" "main" {
  vpc_id = aws_vpc.main.id
  cidr_block = "172.17.1.0/24"
  map_public_ip_on_launch = true
  availability_zone = "us-east-1a"

  tags = {
      Name = "main_subnet"
  }
}

# Main Subnet ACL

resource "aws_network_acl" "main_subnet_acl" {
    vpc_id = aws_vpc.main.id

    egress {
        protocol = "all"
        rule_no = 200
        action = "allow"
        cidr_block = "0.0.0.0/0"
        from_port = 0
        to_port = 0
    } 

    egress {
        protocol = "all"
        rule_no = 201
        action = "allow"
        cidr_block = "172.17.0.0/16"
        from_port = 0
        to_port = 0
    } 
    

    ingress {
        protocol = "all"
        rule_no = 203
        action = "allow"
        cidr_block = "0.0.0.0/0"
        from_port = 0
        to_port = 0
    }

    ingress {
        protocol = "all"
        rule_no = 202
        action = "allow"
        cidr_block = "172.17.0.0/16"
        from_port = 0
        to_port = 0
    }

    tags = {
        Name = "main_subnet_acl"
    }

}

resource "aws_network_acl_association" "main_subnet_nacl_assn" {
    network_acl_id = aws_network_acl.main_subnet_acl.id
    subnet_id = aws_subnet.main.id
  
}

# Main Internet Gateway

resource "aws_internet_gateway" "gw" {
    vpc_id = aws_vpc.main.id

    tags = {
        Name = "gw_main_vpc"
    }
}

# VPC default route table

resource "aws_default_route_table" "main_vpc_rt" {
  default_route_table_id = aws_vpc.main.default_route_table_id

  tags = {
      Name = "main_vpc_rt"
  }
}

#Route to gateway for default route table

resource "aws_route" "main_vpc_gw_route" {
  route_table_id = aws_default_route_table.main_vpc_rt.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id = aws_internet_gateway.gw.id
}

#Route table for main subnet

resource "aws_route_table" "main_subnet_rt" {
  vpc_id = aws_vpc.main.id

  tags = {
      Name = "main_subnet_rt"
  }
}

# Route to my public IP

resource "aws_route" "main_subnet_rt" {
  route_table_id = aws_route_table.main_subnet_rt.id
  destination_cidr_block = "99.107.74.253/32"
  gateway_id = aws_internet_gateway.gw.id
}

resource "aws_route" "main_subnet_rt_internet" {
  route_table_id = aws_route_table.main_subnet_rt.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id = aws_internet_gateway.gw.id
}

# Route association for main subnet route table and main subnet

resource "aws_route_table_association" "main_subnet_rt_assn" {
    subnet_id = aws_subnet.main.id
    route_table_id = aws_route_table.main_subnet_rt.id
  
}

# Windows Server 2019 EC2 instance
data "aws_ami" "Windows" {
  most_recent = true
  
  filter {
    name = "name"
    values = ["Windows_Server-2019-English-Full-Base-*"]
  }

  filter {
    name = "virtualization-type"
    values = ["hvm"]
  }
  owners = ["801119661308"] # Amazon Owner ID
}

resource "aws_instance" "pythonLab" {
  ami = data.aws_ami.Windows.id
  instance_type = "t2.xlarge"
  associate_public_ip_address = true
  subnet_id = aws_subnet.main.id
  key_name = "Py_PS_key_pair"
  vpc_security_group_ids = [aws_security_group.allow_EC2.id]

  lifecycle {
    ignore_changes = [ami]
  }
}

# Security Groups

resource "aws_security_group" "allow_EC2" {
  name = "allow_EC2"
  description = "allow remote access to ec2"
  vpc_id = aws_vpc.main.id

  ingress {
    description      = "remote from home"
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["99.107.74.253/32"]
    
  }


  egress {
    description = "Remote from home"
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["99.107.74.253/32"]
  }
  
  egress {
    description = "HTTPS Outbound"
    from_port        = 443
    to_port          = 443
    protocol         = "TCP"
    cidr_blocks      = ["0.0.0.0/0"]
  }
  egress {
    description = "HTTP Outbound"
    from_port        = 80
    to_port          = 80
    protocol         = "TCP"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
      Name = "allow_ec2"
  }
}
