ALERTS = {
    "5XX_errors_production": {
        "payload": {
            "version": "1.0",
            "incident": {
                "incident_id": "prod-5xx-123",
                "scoping_project_id": "prod-web-cluster",
                "scoping_project_number": 987654,
                "url": "https://console.cloud.google.com/monitoring/alerting/incidents/123",
                "started_at": 0,
                "ended_at": 0,
                "state": "OPEN",
                "summary": "High rate of 5XX errors detected in production environment",
                "apigee_url": "https://console.cloud.google.com/apigee/monitoring",
                "observed_value": "12.5",
                "resource": {
                    "type": "gae_app",
                    "labels": {"module_id": "default", "version_id": "prod-v1"},
                },
                "resource_type_display_name": "App Engine Application",
                "resource_id": "prod-web-cluster",
                "resource_display_name": "Production Web Cluster",
                "resource_name": "projects/987654/apps/prod-web-cluster",
                "metric": {
                    "type": "appengine.googleapis.com/http/server/response_count",
                    "displayName": "Response Count",
                    "labels": {"response_code": "5xx"},
                },
                "metadata": {
                    "system_labels": {"severity": "critical"},
                    "user_labels": {"environment": "production"},
                },
                "policy_name": "projects/987654/alertPolicies/5xx-policy",
                "policy_user_labels": {"team": "platform"},
                "documentation": {
                    "subject": "High rate of 5XX errors detected in production environment",
                },
                "condition": {
                    "name": "projects/987654/alertPolicies/5xx-policy/conditions/1",
                    "displayName": "5XX Error Rate > 5%",
                    "conditionThreshold": {
                        "filter": 'metric.type="appengine.googleapis.com/http/server/response_count" resource.type="gae_app"',
                        "comparison": "COMPARISON_GT",
                        "thresholdValue": 5.0,
                        "duration": "300s",
                        "trigger": {"count": 1},
                    },
                },
                "condition_name": "5XX Error Rate > 5%",
                "threshold_value": "5.0",
            },
        },
        "parameters": {},
    },
    "high_memory_usage": {
        "payload": {
            "version": "1.0",
            "incident": {
                "incident_id": "mem-234",
                "scoping_project_id": "prod-web-cluster",
                "scoping_project_number": 987654,
                "url": "https://console.cloud.google.com/monitoring/alerting/incidents/234",
                "started_at": 0,
                "ended_at": 0,
                "state": "OPEN",
                "summary": "Memory usage exceeds 90% on production servers",
                "observed_value": "92.3",
                "resource": {
                    "type": "gce_instance",
                    "labels": {"instance_id": "prod-web-1"},
                },
                "resource_type_display_name": "GCE VM Instance",
                "resource_id": "prod-web-1",
                "resource_display_name": "Production Web Server 1",
                "resource_name": "projects/987654/instances/prod-web-1",
                "metric": {
                    "type": "compute.googleapis.com/instance/memory/utilization",
                    "displayName": "Memory Utilization",
                    "labels": {},
                },
                "metadata": {
                    "system_labels": {"severity": "warning"},
                    "user_labels": {"environment": "production"},
                },
                "policy_name": "projects/987654/alertPolicies/memory-policy",
                "policy_user_labels": {"team": "platform"},
                "documentation": {
                    "subject": "High memory usage detected",
                },
                "condition": {
                    "name": "projects/987654/alertPolicies/memory-policy/conditions/1",
                    "displayName": "Memory Usage > 90%",
                    "conditionThreshold": {
                        "filter": 'metric.type="compute.googleapis.com/instance/memory/utilization"',
                        "comparison": "COMPARISON_GT",
                        "thresholdValue": 90.0,
                        "duration": "300s",
                        "trigger": {"count": 1},
                    },
                },
                "condition_name": "Memory Usage > 90%",
                "threshold_value": "90.0",
            },
        },
        "parameters": {},
    },
    "database_latency": {
        "payload": {
            "version": "1.0",
            "incident": {
                "incident_id": "db-345",
                "scoping_project_id": "prod-db-cluster",
                "scoping_project_number": 987654,
                "url": "https://console.cloud.google.com/monitoring/alerting/incidents/345",
                "started_at": 0,
                "ended_at": 0,
                "state": "OPEN",
                "summary": "Database query latency above threshold",
                "observed_value": "2.5",
                "resource": {
                    "type": "cloudsql_database",
                    "labels": {"database_id": "prod-mysql-main"},
                },
                "resource_type_display_name": "Cloud SQL Database",
                "resource_id": "prod-mysql-main",
                "resource_display_name": "Production MySQL Main",
                "resource_name": "projects/987654/databases/prod-mysql-main",
                "metric": {
                    "type": "cloudsql.googleapis.com/database/mysql/query_latency",
                    "displayName": "MySQL Query Latency",
                    "labels": {},
                },
                "metadata": {
                    "system_labels": {"severity": "warning"},
                    "user_labels": {"environment": "production"},
                },
                "policy_name": "projects/987654/alertPolicies/db-latency",
                "policy_user_labels": {"team": "database"},
                "documentation": {
                    "subject": "High database query latency detected",
                },
                "condition": {
                    "name": "projects/987654/alertPolicies/db-latency/conditions/1",
                    "displayName": "Query Latency > 2s",
                    "conditionThreshold": {
                        "filter": 'metric.type="cloudsql.googleapis.com/database/mysql/query_latency"',
                        "comparison": "COMPARISON_GT",
                        "thresholdValue": 2.0,
                        "duration": "300s",
                        "trigger": {"count": 1},
                    },
                },
                "condition_name": "Query Latency > 2s",
                "threshold_value": "2.0",
            },
        },
        "parameters": {},
    },
}
