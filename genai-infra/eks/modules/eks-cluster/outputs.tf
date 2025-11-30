output "cluster_name" {
  value       = module.eks.cluster_name
  description = "EKS cluster name"
}

output "cluster_arn" {
  value       = module.eks.cluster_arn
  description = "EKS cluster ARN"
}

output "cluster_endpoint" {
  value       = module.eks.cluster_endpoint
  description = "EKS cluster endpoint"
}

output "cluster_iam_role_arn" {
  value       = module.eks.cluster_iam_role_arn
  description = "Cluster IAM role ARN"
}

output "node_role_arn" {
  value       = try(module.eks.eks_managed_node_groups["cpu"].iam_role_arn, module.eks.worker_iam_role_arn)
  description = "Node group IAM role ARN"
}
