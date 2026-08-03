import { envSchema, type AppEnv } from "./env.schema";

export function loadEnv(rawEnv: NodeJS.ProcessEnv = process.env): AppEnv {
  const parsed = envSchema.safeParse(rawEnv);

  if (!parsed.success) {
    const details = parsed.error.issues
      .map((issue) => `${issue.path.join(".") || "env"}: ${issue.message}`)
      .join("\n");
    throw new Error(`Environment validation failed:\n${details}`);
  }

  return parsed.data;
}

export const env = loadEnv();
