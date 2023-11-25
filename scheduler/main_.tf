provider "google" {
  project = var.project_id
  region  = var.region
}

terraform {
  backend "gcs" {
    bucket  = "terraform-up-and-running-state-tth"
    key     = "stage/scheduled_job/terraform.tfstate"
    region  = "ap-southeast-1"
    profile = "286510118323_AdministratorAccess"

    dynamodb_table = "terraform-up-and-running-locks"
    encrypt        = true
  }
}

module "scheduled_job" {
  source = "github.com/tzehon/terraform_modules//services/scheduled_job?ref=v0.0.1"

  project_id = var.project_id
  service_name = var.service_name
  region = var.region
  url = var.url
}