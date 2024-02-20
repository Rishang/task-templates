
## Table of Contents

- [build_push](#build_push)
    - [summary](#summary)
    - [required variables](#required-variables)
    - [variables](#variables)


## build_push

Build the docker image

#### Summary

Build the docker image and push it to the registry
#### Required Variables

- **REGISTRY**
- **REPOSITORY**
- **PATH**
#### Variables

- **IMAGE_TAG**: `development`
- **STAGE**: `{{default .IMAGE_TAG .STAGE}}`
- **ARGS**: `{{default "" .ARGS}}`
- **USE_BUILDX_PUSH**: `{{default "false" .USE_BUILDX_PUSH}}`
- **CACHE_FROM_LOCAL_PATH**: `{{default "" .CACHE_FROM_LOCAL_PATH}}`


