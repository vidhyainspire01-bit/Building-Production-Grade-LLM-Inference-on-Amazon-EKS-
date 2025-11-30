# 5. Terraform Module: GPU Node Group

# This is your vLLM / Triton runtime.


resource "aws_eks_node_group" "gpu" {
  cluster_name    = var.cluster_name
  node_group_name = "gpu-nodegroup"
  node_role_arn   = var.node_role_arn

  subnet_ids = var.private_subnets

  scaling_config {
    desired_size = 0
    min_size     = 0
    max_size     = 3
  }

  instance_types = ["g5.2xlarge"]
  capacity_type  = "ON_DEMAND"

  tags = {
    Name = "gpu-nodegroup"
  }

  labels = {
    "accelerator" = "nvidia"
  }

  taints = [{
    key    = "nvidia.com/gpu"
    value  = "true"
    effect = "NO_SCHEDULE"
  }]
}
