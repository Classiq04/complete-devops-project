variable "aws_region" {
  description = "AWS region for the EKS deployment"
  type        = string
  default     = "us-east-1"
}

variable "admin_cidr" {
  description = "Public IP allowed to access the EKS API"
  type        = string
  default     = "102.91.103.153/32"
}
