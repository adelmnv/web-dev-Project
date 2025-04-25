export interface LoginResponse {
  access: string;
  refresh: string;
}

export interface RefreshTokenResponse {
  access: string;
}
