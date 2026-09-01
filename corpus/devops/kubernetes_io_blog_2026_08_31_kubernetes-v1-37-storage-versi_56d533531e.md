---
title: "[kubernetes] Kubernetes v1.37: Storage Version Migration Enabled by Default"
url: "https://kubernetes.io/blog/2026/08/31/kubernetes-v1-37-storage-version-migration-ga/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-09-01T06:20:25Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.37: Storage Version Migration Enabled by Default

> Source: devops | Category: infrastructure | 2026-09-01T06:20:25Z

Kubernetes v1.37: Storage Version Migration Enabled by Default

I am excited that  storage version migration  (SVM) has graduated to General Availability (GA) in Kubernetes v1.37! 
 After a number of releases of work and testing, the built-in StorageVersionMigration API ( storagemigration.k8s.io/v1 )
and control plane controller are now fully stable and enabled by default across all v1.37 Kubernetes clusters. 
 The problem with stale storage versions    In Kubernetes, stored API resources are written using a specific  storage version  (schema representation). The way Kubernetes interacts with object storage fundamentally requires mutation of a resource in order to ensure that the latest storage version is used for all resources. This creates problems when you want to change the storage version of a resource. 
 One example of a scenario where you may want to change the storage version of a resource is when you are promoting a CRD to drop an older API version (such as  v1alpha1 ) to a newer version (leaving just  v1beta1  and  v1 ). It's a problem to drop the older API version whilst there are still resources stored with the old alpha version. 
 To avoid problems, you designate  v1  as the new storage version; but, on it's own, that's not enough. While new writes are stored as  v1 , any existing resource could remain stored as  v1alpha1  or  v1beta1  in storage. You cannot safely remove  v1alpha1  from the CRD's  .status.storedVersions  or drop serving support until every single resource in storage has been re-written to not be serialized and stored with the alpha version. 
 Another relevant example is  encryption at rest  and, related,  key rotation .
When you configure encryption at rest or rotate encryption keys, existing resources in storage remain  unencrypted  (or encrypted under old keys) until they are actively
re-written through the Kubernetes API server. 
 Historically, cluster administrators and CRD authors had to rely on manual
 kubectl get  /  kubectl replace  scripts, or to deploy the out-of-tree  kube-storage-vers
