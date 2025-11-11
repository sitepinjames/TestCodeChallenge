locals {
  ecs_tags = {
    Environment  = "Devlp"
    Project      = "Codechalllenge"
    ResourceType = "ecs"
  }

  alb_tags = {
    Environment  = "Devlp"
    Project      = "Codechallenge"
    ResourceType = "elb"
  }

  S3_tags = {
    Environment  = "Devlp"
    Project      = "Codechallenge"
    ResourceType = "S3"
  }


}

