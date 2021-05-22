import { Entity, Column, PrimaryGeneratedColumn } from "typeorm";

@Entity()
class Channel {
  @PrimaryGeneratedColumn()
  id!: number

  @Column({ unique: true, nullable: false })
  server!: string

  @Column({ nullable: false })
  channel!: string
}

export default Channel