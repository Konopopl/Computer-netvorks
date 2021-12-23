#docker cp envoy-config-generated.yml envoy-container:/etc/envoy/envoy.yaml 

if [ -z $1 ];
then
export conf="grpc-envoy.yml"
else
export conf="$1"
fi
echo "$conf"
docker cp "$conf" envoy-container:/etc/envoy/envoy.yaml 
docker exec envoy-container envoy -c /etc/envoy/envoy.yaml --use-dynamic-base-id &