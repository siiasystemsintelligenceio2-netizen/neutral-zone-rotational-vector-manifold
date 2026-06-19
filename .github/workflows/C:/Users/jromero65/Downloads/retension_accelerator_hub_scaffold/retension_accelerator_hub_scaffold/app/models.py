from datetime import datetime, timedelta, timezone
from typing import Any, Literal
from uuid import uuid4

from pydantic import BaseModel, Field


RoutingMode = Literal["alternating", "random", "hash"]
RetentionMode = Literal["post_passive_longevity", "standard", "quarantine"]
Classification = Literal["public", "internal", "confidential", "restricted"]


class QuickLinkPayload(BaseModel):
    """
    Intake model for quick-link hook data.

    content_uri is a pointer/reference, not raw secret data.
    metadata should be limited to authorized, non-sensitive operational metadata.
    """
    account_id: str = Field(..., min_length=3)
    source_id: str = Field(..., min_length=2)
    content_uri: str = Field(..., min_length=3)
    classification: Classification = "internal"
    retention_days: int = Field(default=365, ge=1, le=3650)
    routing: RoutingMode = "alternating"
    mode: RetentionMode = "post_passive_longevity"
    metadata: dict[str, Any] = Field(default_factory=dict)


class InterpretedWorkload(BaseModel):
    workload_id: str = Field(default_factory=lambda: f"wkl_{uuid4().hex}")
    account_id: str
    source_id: str
    content_uri: str
    classification: Classification
    retention_days: int
    mode: RetentionMode
    routing: RoutingMode
    metadata: dict[str, Any]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @property
    def retention_until(self) -> datetime:
        return self.created_at + timedelta(days=self.retention_days)


class IngestResult(BaseModel):
    asset_id: str
    sequence_id: str
    provenance_hash: str
    selected_cell: str
    state: str
    retention_until: datetime
    audit_event: dict[str, Any]


class AssetRecord(BaseModel):
    asset_id: str
    workload: InterpretedWorkload
    sequence_id: str
    provenance_hash: str
    selected_cell: str
    stored_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
