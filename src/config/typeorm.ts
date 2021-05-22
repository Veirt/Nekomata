import { ConnectionOptions } from "typeorm";

const config: ConnectionOptions = {
  type: "sqlite",
  database: "db.sqlite",
  synchronize: true,
  entities: [
    "dist/entity/*{.ts,.js}", "src/entity/*{.ts,.js}"
  ],
  migrations: [
    "dist/migration/*{.ts,.js}", "src/migration/*{.ts,.js}"
  ],
  subscribers: [
    "dist/subscriber/*{.ts,.js}", "src/subscriber/*{.ts,.js}"
  ],
  cli: {
    entitiesDir: "src/entity",
    migrationsDir: "src/migration",
    subscribersDir: "src/subscriber",
  },
}

export default config