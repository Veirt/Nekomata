import Version from "@entity/Version"
import { getConnection } from "typeorm"

export const addPatchInfo = (
  server: string,
  url: string
): Promise<boolean | Error> => {
  return new Promise((resolve, reject) => {
    getConnection()
      .getRepository(Version)
      .save({ server, url })
      .then(() => resolve(true))
      .catch(err => reject(err))
  })
}

export const removePatchInfo = (server: string): Promise<boolean | Error> => {
  return new Promise((resolve, reject) => {
    (async () => {
      try {
        await getConnection().getRepository(Version).findOneOrFail({ server })
        await getConnection().getRepository(Version).delete({ server })
        resolve(true)
      } catch (err) {
        reject(err)
      }
    })()
  })
}

export const findPatchInfo = (): Promise<Version[]> => {
  return new Promise((resolve, reject) => {
    (async () => {
      try {
        const patchInfos = await getConnection().getRepository(Version).find()
        resolve(patchInfos)
      } catch (err) {
        reject(err)
      }
    })()
  })
}
