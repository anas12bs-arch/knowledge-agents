---
title: "[kubernetes] Kubernetes v1.37: Hardening Container Storage with Bind Mount Options and EmptyDir Permissions"
url: "https://kubernetes.io/blog/2026/09/16/kubernetes-v1-37-hardening-container-storage/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-09-17T00:39:09Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.37: Hardening Container Storage with Bind Mount Options and EmptyDir Permissions

> Source: devops | Category: infrastructure | 2026-09-17T00:39:09Z

Kubernetes v1.37: Hardening Container Storage with Bind Mount Options and EmptyDir Permissions

Kubernetes v1.37 brings important storage security features:  emptyDir  permission modes and bind mount options. They help application programmers and security professionals implement rigorous security policies, for example, prohibiting deletion of files across containers or execution of arbitrary binaries from writable volumes, directly in Kubernetes without any complicated circumvention. 
 Linux storage and permission fundamentals    Before diving into the new Kubernetes features, let us briefly review the low-level Linux security mechanisms that make them possible. 
 Bind mount flags    When Linux mounts or remounts a directory, Virtual File System (VFS) flags control what actions are permitted on that filesystem: 
 
   noexec  : Do not permit direct execution of any binaries on the mounted filesystem. 
   nosuid  : Do not allow set-user-identifier or set-group-identifier bits to take effect. 
   nodev  : Do not interpret character or block special devices on the file system. 
 
 Directory permissions and the sticky bit    Standard Unix permissions regulate access across three scopes: Owner, Group, and Others (e.g.,  0755  or  0777 ). 
 Beyond standard read, write, and execute bits, Linux supports the  sticky bit  (as in mode  01777 ).
When applied to a directory, the sticky bit ensures that a file inside that directory can only be deleted or renamed by the file's owner or root. This is essential for shared writable directories like  /tmp . 
 Motivation for the improvements    Why does Kubernetes need bind mount options and  emptyDir  permissions? 
 The primary goal of these features is to increase the security of Kubernetes workloads by allowing security-related bind mount options on volume mounts. By default, volumes are bind-mounted into containers by the container runtime and kubelet without  noexec ,  nosuid , or  nodev  flags. This default can undermine security. For example, with  noexec  missing, a compromised process can use any writable volume ( empty
