import { Entity, Column } from "typeorm";

@Entity()
class Channel {
  @Column({ unique: true, nullable: false })
  server!: string

  @Column({ unique: true, nullable: false })
  channel!: string
}