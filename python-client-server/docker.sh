docker run --rm -it \
      -p 9901:9901 \
      -p 8080:8080 \
      -p 10000:10000 \
      -p 10001:10001 \
      -p 10443:10443 \
      envoyproxy/envoy-dev:b610fba9a94217ed48c939b04278635e7f2b2283 \
          -c /etc/envoy/envoy.yaml \
          --config-yaml "$(cat grpc-envoy.yml)"