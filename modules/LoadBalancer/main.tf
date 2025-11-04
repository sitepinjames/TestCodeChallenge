resource "aws_lb" "cloudchallengealb" {
  name                       = var.albname
  internal                   = false
  load_balancer_type         = "application"
  subnets                    = var.public_subnet_ids # Must span multiple AZs
  security_groups            = [aws_security_group.alb.id]
  enable_deletion_protection = false
  tags                       = var.tags
}
resource "aws_security_group" "alb" {
  name        = "${var.albname}-alb-sg"
  description = "Allow HTTP inbound to ALB"
  vpc_id      = var.vpc_id

  ingress {
    description = "Allow HTTP from anywhere"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["162.120.186.77/32"]
  }

  egress {
    description = "Allow all outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = var.tags
}

resource "aws_lb_target_group" "ecs" {
  name        = "${var.albname}-tg"
  port        = 80
  protocol    = "HTTP"
  target_type = "ip" # Required for Fargate
  vpc_id      = var.vpc_id

  health_check {
    path                = "/"
    protocol            = "HTTP"
    matcher             = "200"
    interval            = 30
    timeout             = 5
    healthy_threshold   = 2
    unhealthy_threshold = 2
  }

  tags = var.tags
}

resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.cloudchallengealb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.ecs.arn
  }
}