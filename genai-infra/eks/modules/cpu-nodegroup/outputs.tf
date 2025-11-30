output "nodegroup_name" {
  value       = aws_eks_node_group.cpu.node_group_name
  description = "CPU node group name"
}

output "nodegroup_id" {
  value       = aws_eks_node_group.cpu.id
  description = "CPU node group ID"
}
