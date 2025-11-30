# 7. Environment Example (Dev)

module "vpc" {
  source              = "../../modules/vpc"
  vpc_cidr            = "10.0.0.0/16"
  public_subnet_cidrs = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnet_cidrs = ["10.0.3.0/24", "10.0.4.0/24"]
  azs = ["us-east-1a", "us-east-1b"]
  project = "genai"
}

module "eks_cluster" {
  source        = "../../modules/eks-cluster"
  cluster_name  = "genai-cluster"
  vpc_id        = module.vpc.vpc_id
  private_subnets = module.vpc.private_subnets
}
module "cpu_nodegroup" {
  source          = "../../modules/cpu-nodegroup"
  cluster_name    = module.eks_cluster.cluster_name
  node_role_arn   = module.eks_cluster.node_role_arn
  private_subnets = module.vpc.private_subnets
}