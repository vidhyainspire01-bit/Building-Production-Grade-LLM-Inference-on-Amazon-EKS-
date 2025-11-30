variable "aws_region" {
  type        = string
  default     = "us-east-1"
  description = "AWS region for resources"
}

variable "environment" {
  type        = string
  default     = "dev"
  description = "Environment name"
}

variable "project" {
  type        = string
  default     = "genai"
  description = "Project name"
}
