/*
  # Zelcry - Crypto Portfolio & Advisory Platform Database Schema

  ## Overview
  Complete database schema for the Zelcry sustainable crypto advisory platform with enhanced features.

  ## New Tables

  ### 1. `user_profiles`
  User profile information and preferences
  - `id` (uuid, primary key)
  - `user_id` (uuid, foreign key to auth.users)
  - `username` (text, unique)
  - `email` (text)
  - `risk_tolerance` (text: Low, Medium, High)
  - `xp_points` (integer, default: 0)
  - `theme_preference` (text: light, dark, auto - default: light)
  - `created_at` (timestamptz)
  - `updated_at` (timestamptz)

  ### 2. `portfolio_assets`
  User cryptocurrency holdings
  - `id` (uuid, primary key)
  - `user_id` (uuid, foreign key to auth.users)
  - `coin_id` (text)
  - `coin_name` (text)
  - `coin_symbol` (text)
  - `quantity` (numeric)
  - `purchase_price` (numeric)
  - `created_at` (timestamptz)
  - `updated_at` (timestamptz)

  ### 3. `crypto_asset_details`
  Detailed information about cryptocurrencies
  - `coin_id` (text, primary key)
  - `name` (text)
  - `symbol` (text)
  - `energy_score` (integer, 0-10)
  - `governance_score` (integer, 0-10)
  - `utility_score` (integer, 0-10)
  - `description` (text)
  - `created_at` (timestamptz)
  - `updated_at` (timestamptz)

  ### 4. `watchlist`
  User's cryptocurrency watchlist
  - `id` (uuid, primary key)
  - `user_id` (uuid, foreign key to auth.users)
  - `coin_id` (text)
  - `coin_name` (text)
  - `coin_symbol` (text)
  - `created_at` (timestamptz)

  ### 5. `price_alerts`
  User-configured price alerts
  - `id` (uuid, primary key)
  - `user_id` (uuid, foreign key to auth.users)
  - `coin_id` (text)
  - `coin_name` (text)
  - `target_price` (numeric)
  - `alert_type` (text: above, below)
  - `is_active` (boolean, default: true)
  - `triggered_at` (timestamptz, nullable)
  - `created_at` (timestamptz)

  ### 6. `ai_conversations`
  AI advisor conversation history
  - `id` (uuid, primary key)
  - `user_id` (uuid, foreign key to auth.users)
  - `message` (text)
  - `response` (text)
  - `created_at` (timestamptz)

  ## Security
  - RLS enabled on all tables
  - Users can only access their own data
  - Crypto asset details are publicly readable

  ## Indexes
  - Optimized for user-specific queries
  - Fast lookups on coin_id and user_id
*/

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- User Profiles Table
CREATE TABLE IF NOT EXISTS user_profiles (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id uuid REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
  username text UNIQUE NOT NULL,
  email text,
  risk_tolerance text DEFAULT 'Low' CHECK (risk_tolerance IN ('Low', 'Medium', 'High')),
  xp_points integer DEFAULT 0,
  theme_preference text DEFAULT 'light' CHECK (theme_preference IN ('light', 'dark', 'auto')),
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);

-- Portfolio Assets Table
CREATE TABLE IF NOT EXISTS portfolio_assets (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id uuid REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
  coin_id text NOT NULL,
  coin_name text NOT NULL,
  coin_symbol text NOT NULL,
  quantity numeric(20, 8) NOT NULL,
  purchase_price numeric(20, 2) NOT NULL,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);

-- Crypto Asset Details Table
CREATE TABLE IF NOT EXISTS crypto_asset_details (
  coin_id text PRIMARY KEY,
  name text NOT NULL,
  symbol text NOT NULL,
  energy_score integer DEFAULT 0 CHECK (energy_score >= 0 AND energy_score <= 10),
  governance_score integer DEFAULT 0 CHECK (governance_score >= 0 AND governance_score <= 10),
  utility_score integer DEFAULT 0 CHECK (utility_score >= 0 AND utility_score <= 10),
  description text DEFAULT '',
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);

-- Watchlist Table
CREATE TABLE IF NOT EXISTS watchlist (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id uuid REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
  coin_id text NOT NULL,
  coin_name text NOT NULL,
  coin_symbol text NOT NULL,
  created_at timestamptz DEFAULT now(),
  UNIQUE(user_id, coin_id)
);

-- Price Alerts Table
CREATE TABLE IF NOT EXISTS price_alerts (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id uuid REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
  coin_id text NOT NULL,
  coin_name text NOT NULL,
  target_price numeric(20, 2) NOT NULL,
  alert_type text NOT NULL CHECK (alert_type IN ('above', 'below')),
  is_active boolean DEFAULT true,
  triggered_at timestamptz,
  created_at timestamptz DEFAULT now()
);

-- AI Conversations Table
CREATE TABLE IF NOT EXISTS ai_conversations (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id uuid REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
  message text NOT NULL,
  response text NOT NULL,
  created_at timestamptz DEFAULT now()
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_user_profiles_user_id ON user_profiles(user_id);
CREATE INDEX IF NOT EXISTS idx_portfolio_assets_user_id ON portfolio_assets(user_id);
CREATE INDEX IF NOT EXISTS idx_portfolio_assets_coin_id ON portfolio_assets(coin_id);
CREATE INDEX IF NOT EXISTS idx_watchlist_user_id ON watchlist(user_id);
CREATE INDEX IF NOT EXISTS idx_price_alerts_user_id ON price_alerts(user_id);
CREATE INDEX IF NOT EXISTS idx_price_alerts_active ON price_alerts(is_active) WHERE is_active = true;
CREATE INDEX IF NOT EXISTS idx_ai_conversations_user_id ON ai_conversations(user_id);
CREATE INDEX IF NOT EXISTS idx_ai_conversations_created_at ON ai_conversations(created_at DESC);

-- Enable Row Level Security
ALTER TABLE user_profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE portfolio_assets ENABLE ROW LEVEL SECURITY;
ALTER TABLE crypto_asset_details ENABLE ROW LEVEL SECURITY;
ALTER TABLE watchlist ENABLE ROW LEVEL SECURITY;
ALTER TABLE price_alerts ENABLE ROW LEVEL SECURITY;
ALTER TABLE ai_conversations ENABLE ROW LEVEL SECURITY;

-- User Profiles Policies
CREATE POLICY "Users can view own profile"
  ON user_profiles FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own profile"
  ON user_profiles FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update own profile"
  ON user_profiles FOR UPDATE
  TO authenticated
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can delete own profile"
  ON user_profiles FOR DELETE
  TO authenticated
  USING (auth.uid() = user_id);

-- Portfolio Assets Policies
CREATE POLICY "Users can view own portfolio"
  ON portfolio_assets FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own portfolio assets"
  ON portfolio_assets FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update own portfolio assets"
  ON portfolio_assets FOR UPDATE
  TO authenticated
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can delete own portfolio assets"
  ON portfolio_assets FOR DELETE
  TO authenticated
  USING (auth.uid() = user_id);

-- Crypto Asset Details Policies (Public Read)
CREATE POLICY "Anyone can view crypto details"
  ON crypto_asset_details FOR SELECT
  TO authenticated
  USING (true);

CREATE POLICY "Service role can manage crypto details"
  ON crypto_asset_details FOR ALL
  TO service_role
  USING (true)
  WITH CHECK (true);

-- Watchlist Policies
CREATE POLICY "Users can view own watchlist"
  ON watchlist FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

CREATE POLICY "Users can add to own watchlist"
  ON watchlist FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can delete from own watchlist"
  ON watchlist FOR DELETE
  TO authenticated
  USING (auth.uid() = user_id);

-- Price Alerts Policies
CREATE POLICY "Users can view own alerts"
  ON price_alerts FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

CREATE POLICY "Users can create own alerts"
  ON price_alerts FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update own alerts"
  ON price_alerts FOR UPDATE
  TO authenticated
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can delete own alerts"
  ON price_alerts FOR DELETE
  TO authenticated
  USING (auth.uid() = user_id);

-- AI Conversations Policies
CREATE POLICY "Users can view own conversations"
  ON ai_conversations FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

CREATE POLICY "Users can create own conversations"
  ON ai_conversations FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for updated_at
CREATE TRIGGER update_user_profiles_updated_at
  BEFORE UPDATE ON user_profiles
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_portfolio_assets_updated_at
  BEFORE UPDATE ON portfolio_assets
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_crypto_asset_details_updated_at
  BEFORE UPDATE ON crypto_asset_details
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at_column();
