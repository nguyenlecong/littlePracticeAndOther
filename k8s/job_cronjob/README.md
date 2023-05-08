# How to automatically remove completed Kubernetes Pods/Jobs created by a CronJob?

## 1. Set **"CronJob.spec.successfulJobsHistoryLimit: 0"**

## or/and

## 2. Set **"CronJob.spec.jobTemplate.spec.ttlSecondsAfterFinished: 0"**

| Id  | _successfulJobsHistoryLimit_ | _ttlSecondsAfterFinished_ | Automatically Remove? |
| :-: | :--------------------------: | :-----------------------: | --------------------- |
|  1  |              0               |           None            | Yes                   |
|  2  |             None             |             0             | Yes                   |
|  3  |              0               |             0             | Yes                   |
|  4  |              0               |            10             | Yes                   |
|  5  |              3               |             0             | Yes                   |

# ... Please refer to the example code ...

## - Create the Cronjob: _kubectl apply -f cronjob.yaml_

## - Get Cronjob: _(watch -n 1) kubectl get cronjob -o wide_

## - Get Job: _(watch -n 1) kubectl get job -o wide_

## - Get Pod: _(watch -n 1) kubectl get pod -o wide_

(_watch -n X_ - Repeat a Linux Command Every X Seconds Forever)
