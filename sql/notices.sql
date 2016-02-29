CREATE   TABLE  notices
(        id             SERIAL          PRIMARY  KEY
,        title          VARCHAR  ( 500) NOT NULL
,        content        TEXT            NOT NULL
,        action         VARCHAR  ( 100)     NULL
,        image_path     VARCHAR  ( 255)     NULL
,        is_scheduled   BOOLEAN         NOT NULL DEFAULT FALSE
,        scheduled_at   TIMESTAMP           NULL DEFAULT NOW()
,        created_at     TIMESTAMP       NOT NULL DEFAULT NOW()
,        updated_at     TIMESTAMP       NOT NULL DEFAULT NOW()
);