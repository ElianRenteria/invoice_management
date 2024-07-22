const APIConfig = {
  protocol: "http",
  host: "localhost",
  port: 3000,
  basePath: "/api/v2",

  baseURL() {
    return `${this.protocol}://${this.host}:${this.port}${this.basePath}`;
  },
};

export default APIConfig;
