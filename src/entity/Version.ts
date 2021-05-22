import { Entity, Column, PrimaryGeneratedColumn } from "typeorm";

@Entity()
class Version {
  @PrimaryGeneratedColumn()
  id!: number

  @Column({ unique: true, nullable: false })
  server!: string

  @Column({ nullable: false })
  version!: number
}

export default Version