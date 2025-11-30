variable "vpc_cidr" {
  type        = string
  description = "CIDR block for the VPC"
}

variable "public_subnet_cidrs" {
  type        = list(string)
  description = "CIDR blocks for public subnets"
}

variable "private_subnet_cidrs" {
  type        = list(string)
  description = "CIDR blocks for private subnets"
}

variable "azs" {
  type        = list(string)
  description = "Availability zones for subnets"
}

variable "project" {
  type        = string
  description = "Project name for tagging"
}

variable "environment" {
  type        = string
  default     = "dev"
  description = "Environment name"
}
