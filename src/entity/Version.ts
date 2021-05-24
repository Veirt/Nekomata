import { Entity, Column, PrimaryGeneratedColumn } from "typeorm"

@Entity()
class Version {
	@PrimaryGeneratedColumn()
	id!: number

	@Column({ unique: true, nullable: false })
	server!: string

	@Column({ nullable: true })
	version!: number

	@Column({ nullable: false })
	url!: string
}

export default Version
