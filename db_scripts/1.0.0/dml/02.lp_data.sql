INSERT INTO "public"."login_providers" ("name", "type", "description", "login_button_text", "login_button_image_url", "authorization_parameters", "created_at", "updated_at", "id", "active", "strategy_id") VALUES
('E Signet', 'oauth2_auth_code', 'e-signet', 'PROCEED WITH NATIONAL ID', 'https://login.url', '{
  "authorize_endpoint": "https://esignet.openg2p.sandbox.net/authorize",
  "token_endpoint": "https://esignet.openg2p.sandbox.net/v1/esignet/oauth/v2/token",
  "validate_endpoint": "https://esignet.openg2p.sandbox.net/v1/esignet/oidc/userinfo",
  "jwks_endpoint": "https://esignet.openg2p.sandbox.net/v1/esignet/oauth/.well-known/jwks.json",
  "client_id": "",
  "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
  "client_assertion_jwk": {},
  "response_type": "code",
  "scope": "openid profile email",
  "redirect_uri": "http://selfservice.qa.openg2p.net/api/selfservice/oauth2/callback",
  "code_verifier": "",
  "extra_authorize_parameters": {
    "acr_values":"mosip:idp:acr:generated-code mosip:idp:acr:biometrics mosip:idp:acr:linked-wallet",
    "claims": "{\"userinfo\":{\"name\":{\"essential\":true},\"phone_number\":{\"essential\":false},\"email\":{\"essential\":false},\"gender\":{\"essential\":true},\"birthdate\":{\"essential\":true},\"address\":{\"essential\":false},\"picture\":{\"essential\":false}},\"id_token\":{}}"
  }
}', '2024-04-22 12:14:52.174414', '2024-04-22 12:14:52.174414', 1, 't', 1) ON CONFLICT DO NOTHING;
