
# 6. Add-ons Module (KEDA, EBS CSI, etc.)

module "eks_blueprints_addons" {
  source = "aws-ia/eks-blueprints-addons/aws"

  cluster_name      = var.cluster_name
  cluster_endpoint  = var.cluster_endpoint
  cluster_version   = var.cluster_version
  oidc_provider_arn = var.oidc_provider_arn

  enable_keda               = true
  enable_metrics_server     = true
  enable_ebs_csi_driver     = true
  enable_aws_load_balancer_controller = true
}
