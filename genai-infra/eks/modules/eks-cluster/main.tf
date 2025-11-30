# Terraform Module: EKS Cluster (NO GPU YET)

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = var.cluster_name

  vpc_id     = var.vpc_id
  subnet_ids = var.private_subnets

  enable_irsa = true

  tags = {
    Environment = var.environment
  }
}
