variable "expected_image_tag" {
  type = string
}

variable "actual_image_tag" {
  type = string
}
output "image_tag_match" {
  value = var.expected_image_tag == var.actual_image_tag
}


