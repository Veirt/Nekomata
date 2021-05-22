import { ConnectionOptions } from "typeorm";

const config: ConnectionOptions = {
  type: "sqlite",
  database: "db.sqlite",
  synchronize: true,
}

export default config