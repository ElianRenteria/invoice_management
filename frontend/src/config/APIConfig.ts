const APIConfig = {
  protocol: "http",
  host: "localhost",
  port: 8080,
  basePath: "/api/v1",

  baseURL() {
    return `${this.protocol}://${this.host}:${this.port}${this.basePath}`;
  },
};

export default APIConfig;
