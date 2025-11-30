# 4. Terraform Module: CPU Node Group

# This runs:

# Inference gateway

# ChromaDB

# Redis

# LangGraph agents

# System pods


resource "aws_eks_node_group" "cpu" {
  cluster_name    = var.cluster_name
  node_group_name = "cpu-nodegroup"
  node_role_arn   = var.node_role_arn

  subnet_ids = var.private_subnets

  scaling_config {
    desired_size = 2
    min_size     = 2
    max_size     = 4
  }

  instance_types = ["t3.large"]
  capacity_type  = "ON_DEMAND"

  tags = {
    Name = "cpu-nodegroup"
  }
}
