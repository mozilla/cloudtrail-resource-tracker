# cloudtrail-resource-tracker

## Problem Statement
During investigation and incident response, it is difficult to determine an owner/operator/admin for a given AWS resource (account, EC2 instance, database, etc.).

## Possible Solution
Develop a searchable database that automatically maps resources to humans that create those resources, and build a simple way to query that database

## How?
* We consume CloudTrail logs for most of Mozilla’s AWS infrastructure (excluding Firefox Services). These logs contain information on AWS users and resources
  * Once MAWS is deployed, the AWS users will map to canonical LDAP identities for staff
* CloudTrail logs in MozDef are only around for a month, meaning history doesn’t persist for as long as we might need during investigation and incident

## Approach
1. At a regular schedule, query CloudTrail for the following event types:
   * Resource Creation
   * Resource Deletion
1. Transform returned Creation events and inject into relational database
   * Map AWS Resource to
     * Associated AWS account
     * Each human that touched it
       * Last time they touched it (we only care about recency, because we’re trying to find the most relevant human)
       * Last action they took or preserve who created it
1. For returned Deletion events, ~~remove the resource from the database~~ mark as deleted, but keep for historical reasons.
