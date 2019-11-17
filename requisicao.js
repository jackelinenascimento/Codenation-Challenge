const url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=39f5292cbc6779850aff60de8066b92ed244ecd1'

const puxar = new XMLHttpRequest();
puxar.open("GET", url);
puxar.send();

console.log(puxar.responseText);