variable "cluster_name" {
  type        = string
  description = "EKS cluster name"
}

variable "node_role_arn" {
  type        = string
  description = "IAM role ARN for node group"
}

variable "private_subnets" {
  type        = list(string)
  description = "Private subnet IDs for node group"
}
