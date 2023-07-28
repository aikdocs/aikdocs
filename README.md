# aikdocs

The aikdocs project aims to build a smart knowledge base by training those docs from CNCF projects with ChatGPT.

All are starting from a scratch currently. We welcome all contributors from anywhere.

The efforts of the initial roadmap include:

1. Create a [docs-pool](./pool/README.md) from all docs of CNCF projects
1. Build a model to train those docs
1. Provide a web portal to be easily used by anyone

![cover](./images/aikdocs1.jpg)

## Community, discussion, contribution, and support

Any PRs and issues are welcome on GitHub. You can reach the maintainers of this project at:

- [Slack](https://app.slack.com/huddle/T08PSQ7BQ/C05H1HQJGEB)

### Code of conduct

Participation in the aikdocs community is governed by the [aikdocs Code of Conduct](code-of-conduct.md).

## Roadmap

aikdocs has a roadmap as follows:

- [ ] Training those docs from CNCF graduated, incubating, and sandbox projects
- [ ] Improve the dataset (/dataset/*.csv) after the initial training
- [ ] Set up a mechanism to follow up the daily update to each repo
- [ ] Find a more strong and easy-to-use ChatGPT model than current FastGPT, which is relatively weak and cannot provide an English UI
- [ ] Use a short URL rather than https://fastgpt.daocloud.io/chat/share?shareId=64c07d3839dc3432b7bde5a2
- [ ] Build a user-friendly UI with useful prompt options

### CNCF Graduated

Most graduated projects provide markdown files, so it's relatively easy to perform ChatGPT learning and training.

| Items   | Projects      | Progress |
| ------- | ------------- | -------- |
| Docs    | K8s           | &check;  |
| Blog    | K8s           | &check;  |
| Docs    | Istio         | &check;  |
| Blog    | Istio         | &check;  |
| News    | Istio         | &check;  |
| Docs    | Argo          | &check;  |
| Blog    | Argo          | &check;  |
| Docs    | containerd    | &check;  |
| Docs    | CoreDNS       | &check;  |
| Blog    | CoreDNS       | &check;  |
| Website | CRI-O         | &check;  |
| Docs    | envoy         | &check;  |
| Blog    | envoy         | &check;  |
| Docs    | etcd          | &check;  |
| Blog    | etcd          | &check;  |
| Docs    | fluentd       | &check;  |
| Blog    | fluentd       | &check;  |
| Docs    | flux          | &check;  |
| Blog    | flux          | &check;  |
| Docs    | Harbor        | &check;  |
| Blog    | Harbor        | &check;  |
| Docs    | Helm          | &check;  |
| Blog    | Helm          | &check;  |
| Docs    | Jaeger        | &check;  |
| Blog    | Jaeger        | &check;  |
| Docs    | Linkerd       | &check;  |
| Blog    | Linkerd       | &check;  |
| Docs    | Prometheus    | &check;  |
| Blog    | Prometheus    | &check;  |
| Docs    | Rook-ceph     | &check;  |
| Blog    | Rook-ceph     | &check;  |
| Docs    | Spiffe        | &check;  |
| Docs    | Spire         | &check;  |
| Docs    | CNCF Glossary | &check;  |

### CNCF Incubation

| Items   | Projects           | Progress |
| ------- | ------------------ | -------- |
| Docs    | Backstage          |          |
| Blog    | Backstage          |          |
| Docs    | Buildpacks         |          |
| Blog    | Buildpacks         |          |
| Docs    | cert-manager       |          |
| Docs    | Chaos Mesh         |          |
| Blog    | Chaos Mesh         |          |
| Docs    | Cilium             |          |
| Docs    | Cloud Custodian    |          |
| Website | CloudEvents        |          |
| Docs    | CNI                |          |
| Docs    | Contour            |          |
| Blog    | Contour            |          |
| Docs    | Cortex             |          |
| Docs    | Crossplane         |          |
| Blog    | Crossplane         |          |
| Website | CubeFS             |          |
| Website | Dapr               |          |
| Website | Dragonfly          |          |
| Website | Emissary-Ingress   |          |
| Website | Falco              |          |
| Website | gRPC               |          |
| Website | in-toto            |          |
| Website | Karmada            |          |
| Website | Keda               |          |
| Website | Keptn              |          |
| Website | Keycloak           |          |
| Website | Knative            |          |
| Website | KubeEdge           |          |
| Website | KubeVela           |          |
| Website | KubeVirt           |          |
| Website | Kyverno            |          |
| Website | Litmus             |          |
| Website | Longhorn           |          |
| Website | NATS               |          |
| Website | Notary             |          |
| Website | OpenKruise         |          |
| Website | OpenMetrics        |          |
| Website | OpenTelemetry      |          |
| Intro   | Operator Framework |          |
| Website | Thanos             |          |
| Website | Volcano            |          |

### CNCF Sandbox

| Items   | Projects                | Progress |
| ------- | ----------------------- | -------- |
| Website | Aeraki Mesh             |          |
| Docs    | Akri                    |          |
| Website | Antrea                  |          |
| Website | Armada                  |          |
| Website | Artifact Hub            |          |
| Website | Athenz                  |          |
| Website | BFE                     |          |
| Website | Carina                  |          |
| Website | Carvel                  |          |
| Website | CDK for Kubernetes      |          |
| Website | Chaosblade              |          |
| Website | Clusternet              |          |
| Website | Clusterpedia            |          |
| Website | CNI-Genie               |          |
| Docs    | Confidential Containers |          |
| Website | ContainerSSH            |          |
| Website | Curiefense              |          |
| Website | Curve                   |          |
| Website | Devfile                 |          |
| Website | DevSpace                |          |
