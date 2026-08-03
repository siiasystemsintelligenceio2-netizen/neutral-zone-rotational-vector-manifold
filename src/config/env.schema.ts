import { z } from "zod";

const nonEmpty = (field: string) => z.string().min(1, `${field} is required`);

export const envSchema = z.object({
  NODE_ENV: z.enum(["development", "staging", "production"]),
  APP_ENV: z.enum(["development", "staging", "production"]),
  PORT: z.coerce.number().int().min(1).max(65535),
  DATABASE_URL: z.string().url("DATABASE_URL must be a valid URL"),
  REDIS_URL: z.string().url("REDIS_URL must be a valid URL"),
  JWT_SECRET: nonEmpty("JWT_SECRET").min(32, "JWT_SECRET must be at least 32 characters"),
  SENTRY_DSN: z.string().url("SENTRY_DSN must be a valid URL"),
  OTEL_EXPORTER_OTLP_ENDPOINT: z.string().url("OTEL_EXPORTER_OTLP_ENDPOINT must be a valid URL"),
  LOG_LEVEL: z.enum(["debug", "info", "warn", "error"]),
  RATE_LIMIT_RPS: z.coerce.number().positive("RATE_LIMIT_RPS must be > 0"),
  FEATURE_FLAGS_JSON: nonEmpty("FEATURE_FLAGS_JSON"),
  AI_RETENTION_STORE_URL: z.string().url("AI_RETENTION_STORE_URL must be a valid URL"),
  AI_RETENTION_ENCRYPTION_KEY: nonEmpty("AI_RETENTION_ENCRYPTION_KEY").min(
    32,
    "AI_RETENTION_ENCRYPTION_KEY must be at least 32 characters"
  ),
  AI_RETENTION_TTL_DAYS: z.coerce.number().int().positive(),
  AI_REDACTION_MODE: z.enum(["strict", "balanced"]),
  DEPLOY_SHA: nonEmpty("DEPLOY_SHA"),
  SERVICE_VERSION: nonEmpty("SERVICE_VERSION"),
});

export type AppEnv = z.infer<typeof envSchema>;
