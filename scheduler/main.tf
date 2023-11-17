provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_project_service" "run_api" {
  service            = "run.googleapis.com"
  disable_on_destroy = false
}

resource "google_project_service" "iam_api" {
  service            = "iam.googleapis.com"
  disable_on_destroy = false
}

resource "google_cloud_run_v2_service" "default" {
  name     = var.service_name
  location = var.region

  template {
    containers {
      image = var.url
    }
  }

  # Use an explicit depends_on clause to wait until API is enabled
  depends_on = [
    google_project_service.run_api
  ]
}

output "service_url" {
  value = google_cloud_run_v2_service.default.uri
}

resource "google_service_account" "default" {
  account_id   = "scheduler-sa"
  description  = "Cloud Scheduler service account; used to trigger scheduled Cloud Run jobs."
  display_name = "scheduler-sa"

  depends_on = [
    google_project_service.iam_api
  ]
}

resource "google_cloud_run_service_iam_member" "default" {
  location = google_cloud_run_v2_service.default.location
  service  = google_cloud_run_v2_service.default.name
  role     = "roles/run.invoker"
  member   = "serviceAccount:${google_service_account.default.email}"
}