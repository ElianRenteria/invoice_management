export type Client = {
  id: number; // Unique identifier for the client
  name: string; // Full name of the client or company
  email: string; // Primary contact email
  phone?: string; // Primary contact phone number
  facsimile?: string; // Facsimile or fax number
  created_by: number; // ID of the user who created this client record
  contact_person?: string; // Name of the primary contact person for the client
  company_name?: string; // Company name, if applicable
  industry?: string; // Industry in which the client operates
  website?: string; // Client's website URL
  notes?: string; // Additional notes about the client
  created_at?: Date; // Timestamp when the client was created
  updated_at?: Date; // Timestamp when the client was last updated
  status: ClientStatus; // Status of the client, useful for deactivating or archiving
  address_line1?: string; // Address line 1
  address_line2?: string; // Address line 2
  address_city?: string; // City
  address_state?: string; // State or province
  address_postal_code?: string; // Postal code or ZIP code
  address_country?: string; // Country
  billing_address_line1?: string; // Billing address line 1
  billing_address_line2?: string; // Billing address line 2
  billing_address_city?: string; // Billing city
  billing_address_state?: string; // Billing state or province
  billing_address_postal_code?: string; // Billing postal code or ZIP code
  billing_address_country?: string; // Billing country
};

export type ClientStatus = "active" | "inactive";

export const clientStatusOptions = [
  { value: "active", label: "Active" },
  { value: "inactive", label: "Inactive" },
];
