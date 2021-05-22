import { ConnectionOptions } from "typeorm";

const config: ConnectionOptions = {
  type: "sqlite",
  database: "db.sqlite",
  synchronize: true,
  entities: [
    process.env.NODE_ENV === "production"
      ? "dist/entity/*{.ts,.js}"
      : "src/entity/*{.ts,.js}",
  ],
  migrations: [
    process.env.NODE_ENV === "production"
      ? "dist/migration/*{.ts,.js}"
      : "src/migration/*{.ts,.js}",
  ],
  subscribers: [
    process.env.NODE_ENV === "production"
      ? "dist/subscriber/*{.ts,.js}"
      : "src/subscriber/*{.ts,.js}",
  ],
  cli: {
    entitiesDir: "src/entity",

    migrationsDir: "src/migration",
    subscribersDir: "src/subscriber",
  },
}

export default config