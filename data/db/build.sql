CREATE TABLE IF NOT EXISTS guilds (
	GuildID integer PRIMARY KEY,
	Prefix text DEFAULT "sayu "
);

CREATE TABLE IF NOT EXISTS operators (
	UserID integer PRIMARY KEY,
	Username text
);

CREATE TABLE IF NOT EXISTS exp (
	UserID integer PRIMARY KEY,
	XP integer DEFAULT 0,
	Level integer DEFAULT 0,
	XPLock text DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS welcome (
	GuildID integer PRIMARY KEY,
	Link text,
	Message text,
	Footer text
);

CREATE TABLE IF NOT EXISTS leave (
	GuildID integer PRIMARY KEY,
	Link text,
	Message text,
	Footer text
);

CREATE TABLE IF NOT EXISTS mutes (
	UserID integer PRIMARY KEY,
	RoleIDs text,
	EndTime text
);

CREATE TABLE IF NOT EXISTS warnings(
	UserID integer PRIMARY KEY,
	NoOfWarns integer DEFAULT 0,
	R1 text,
	R1_Mod text,
	R1_Date text,
	R2 text,
	R2_Mod text,
	R2_Date text,
	R3 text,
	R3_Mod text,
	R3_Date text,
	R4 text,
	R4_Mod text,
	R4_Date text,
	R5 text,
	R5_Mod text,
	R5_Date text
);

CREATE TABLE IF NOT EXISTS starboard(
	RootMessageID integer PRIMARY KEY,
	StarMessageID integer,
	Stars integer DEFAULT 1
);

