--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: item_id_seq; Type: SEQUENCE; Schema: public; Owner: mvp
--

CREATE SEQUENCE public.item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.item_id_seq OWNER TO mvp;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: items; Type: TABLE; Schema: public; Owner: mvp
--

CREATE TABLE public.items (
    transaction_id bigint NOT NULL,
    transaction_type character varying DEFAULT 'Insert'::character varying NOT NULL,
    item_id bigint NOT NULL,
    title character varying DEFAULT ''::character varying NOT NULL,
    details character varying DEFAULT ''::character varying NOT NULL,
    important boolean DEFAULT false NOT NULL,
    arb_order bigint DEFAULT 0 NOT NULL,
    "timestamp" bigint NOT NULL
);


ALTER TABLE public.items OWNER TO mvp;

SET default_tablespace = listappdevspace;

--
-- Name: loggedinusers; Type: TABLE; Schema: public; Owner: mvp; Tablespace: listappdevspace
--

CREATE TABLE public.loggedinusers (
    token character varying,
    user_id bigint
);


ALTER TABLE public.loggedinusers OWNER TO mvp;

SET default_tablespace = '';

--
-- Name: user_1623064154309668000; Type: TABLE; Schema: public; Owner: mvp
--

CREATE TABLE public.user_1623064154309668000 (
    transaction_id bigint,
    transaction_type character varying,
    item_id bigint,
    title character varying,
    details character varying,
    important boolean,
    arb_order bigint,
    "timestamp" bigint
);


ALTER TABLE public.user_1623064154309668000 OWNER TO mvp;

--
-- Name: user_1624005566093007000; Type: TABLE; Schema: public; Owner: mvp
--

CREATE TABLE public.user_1624005566093007000 (
    transaction_id bigint,
    transaction_type character varying,
    item_id bigint,
    title character varying,
    details character varying,
    important boolean,
    arb_order bigint,
    "timestamp" bigint
);


ALTER TABLE public.user_1624005566093007000 OWNER TO mvp;

--
-- Name: user_1625062406786100000; Type: TABLE; Schema: public; Owner: mvp
--

CREATE TABLE public.user_1625062406786100000 (
    transaction_id bigint,
    transaction_type character varying,
    item_id bigint,
    title character varying,
    details character varying,
    important boolean,
    arb_order bigint,
    "timestamp" bigint
);


ALTER TABLE public.user_1625062406786100000 OWNER TO mvp;

--
-- Name: user_1625067036221060000; Type: TABLE; Schema: public; Owner: mvp
--

CREATE TABLE public.user_1625067036221060000 (
    transaction_id bigint,
    transaction_type character varying,
    item_id bigint,
    title character varying,
    details character varying,
    important boolean,
    arb_order bigint,
    "timestamp" bigint
);


ALTER TABLE public.user_1625067036221060000 OWNER TO mvp;

--
-- Name: user_1625079515986807000; Type: TABLE; Schema: public; Owner: mvp
--

CREATE TABLE public.user_1625079515986807000 (
    transaction_id bigint,
    transaction_type character varying,
    item_id bigint,
    title character varying,
    details character varying,
    important boolean,
    arb_order bigint,
    "timestamp" bigint
);


ALTER TABLE public.user_1625079515986807000 OWNER TO mvp;

--
-- Name: user_1625305455770794000; Type: TABLE; Schema: public; Owner: mvp
--

CREATE TABLE public.user_1625305455770794000 (
    transaction_id bigint,
    transaction_type character varying,
    item_id bigint,
    title character varying,
    details character varying,
    important boolean,
    arb_order bigint,
    "timestamp" bigint
);


ALTER TABLE public.user_1625305455770794000 OWNER TO mvp;

--
-- Name: user_1625305602467790000; Type: TABLE; Schema: public; Owner: mvp
--

CREATE TABLE public.user_1625305602467790000 (
    transaction_id bigint,
    transaction_type character varying,
    item_id bigint,
    title character varying,
    details character varying,
    important boolean,
    arb_order bigint,
    "timestamp" bigint
);


ALTER TABLE public.user_1625305602467790000 OWNER TO mvp;

--
-- Name: user_empty_table; Type: TABLE; Schema: public; Owner: mvp
--

CREATE TABLE public.user_empty_table (
    transaction_id bigint,
    transaction_type character varying,
    item_id bigint,
    title character varying,
    details character varying,
    important boolean,
    arb_order bigint,
    "timestamp" bigint
);


ALTER TABLE public.user_empty_table OWNER TO mvp;

SET default_tablespace = listappdevspace;

--
-- Name: users; Type: TABLE; Schema: public; Owner: mvp; Tablespace: listappdevspace
--

CREATE TABLE public.users (
    user_id bigint NOT NULL,
    email character varying,
    pass_hash character varying,
    profile character varying
);


ALTER TABLE public.users OWNER TO mvp;

--
-- Data for Name: items; Type: TABLE DATA; Schema: public; Owner: mvp
--

COPY public.items (transaction_id, transaction_type, item_id, title, details, important, arb_order, "timestamp") FROM stdin;
1622736919300	Add	1622736919298	Bread	Details	f	8965	1622736919298
1622736922568	Add	1622736922568	Banana	Details	f	85654	1622736922568
1622736988619	Add	1622736988618	Canopy	Details	f	85103	1622736988618
1622737005753	Add	1622737005753	Watermelon	Details	f	9745	1622737005753
1622737259992	Modify	1622736988618	Canopy	Details	t	85103	1622737259990
1622737355702	Modify	1622736922568	Banana	Details	t	85654	1622737355700
1622737478588	Modify	1622736922568	Banana	Details	f	85654	1622737478587
1622737479482	Modify	1622736922568	Banana	Details	t	85654	1622737479482
1622737532745	Remove	1622736988618	Canopy	Details	t	85103	1622737259990
1622737547584	Add	1622737547583	Hello	Details	f	26955	1622737547583
1622737962524	Modify	1622737547583	Hello	Details	t	26955	1622737962523
1622738014877	Modify	1622737005753	Watermelon	Details	t	9745	1622738014877
1622738059688	Add	1622738059687	Clicky	Details	f	68277	1622738059687
1622738086997	Add	1622738086997	A	Details	f	21624	1622738086997
1622738089459	Add	1622738089459	B	Details	f	86704	1622738089459
1622738091343	Modify	1622738086997	A	Details	t	21624	1622738091343
1622738969733	Remove	1622737547583	Hello	Details	t	26955	1622737962523
1622876845444	Add	1622876845442	Big	Details	f	58542	1622876845442
1622876965221	Add	1622876965221	Samsung	Details	f	51851	1622876965221
1622876992205	Add	1622876992205	Bag	Details	f	62182	1622876992205
1622877003669	Modify	1622876965221	Samsung	Details	t	51851	1622877003668
1622877007189	Modify	1622876992205	Bag	Details	t	62182	1622877007189
1622877008110	Modify	1622876992205	Bag	Details	f	62182	1622877008109
1622877008738	Modify	1622876992205	Bag	Details	t	62182	1622877008738
1622877009402	Modify	1622876992205	Bag	Details	f	62182	1622877009402
1622877010418	Modify	1622876992205	Bag	Details	t	62182	1622877010417
1622877012088	Modify	1622876992205	Bag	Details	f	62182	1622877012088
1622877275526	Modify	1622738089459	B	Details	t	86704	1622877275525
1622877333730	Modify	1622738059687	Clicky	Details	t	68277	1622877333730
1622877875998	Add	1622877875998	Trick	details	f	0	1622877875998
1622877891761	Modify	1622877875998	Trick	details	t	0	1622877891761
1622877893662	Modify	1622877875998	Trick	details	f	0	1622877893662
1622877894809	Modify	1622877875998	Trick	details	t	0	1622877894809
1622877895449	Modify	1622877875998	Trick	details	f	0	1622877895449
1622877897507	Modify	1622876992205	Bag	Details	t	62182	1622877897505
1622877898468	Modify	1622876992205	Bag	Details	f	62182	1622877898468
1622909692645	Modify	1622738089459	B	Details	f	86704	1622909692644
1622909693650	Modify	1622738089459	B	Details	t	86704	1622909693650
1622910101472	Modify	1622737005753	Watermelon	Details	f	9745	1622910101472
1622910102077	Modify	1622737005753	Watermelon	Details	t	9745	1622910102077
1622910138957	Remove	1622738059687	Clicky	Details	t	68277	1622877333730
1622910197186	Add	1622910197185	Biscuit	details	f	0	1622910197185
1622910213254	Remove	1622876992205	Bag	Details	f	62182	1622877898468
1622910216851	Remove	1622876965221	Samsung	Details	t	51851	1622877003668
1622910218324	Remove	1622876845442	Big	Details	f	58542	1622876845442
1622910241012	Add	1622910241012	Almond	details	f	0	1622910241012
1622910348088	Remove	1622738086997	A	Details	t	21624	1622738091343
1622910351242	Remove	1622738089459	B	Details	t	86704	1622909693650
1622910382882	Modify	1622910197185	Biscuit	details	t	0	1622910382882
1622910383396	Modify	1622910197185	Biscuit	details	f	0	1622910383396
1622911073898	Modify	1622737005753	Watermelon	Details	f	9745	1622911073898
1622911074584	Modify	1622737005753	Watermelon	Details	t	9745	1622911074584
1623042131553	Modify	1622910197185	Biscuit	details	t	0	1623042131553
1623042136617	Modify	1622910197185	Biscuit	details	f	0	1623042136617
1623042139089	Remove	1622877875998	Trick	details	f	0	1622877895449
1624002650785	Remove	1622737005753	Watermelon	Details	t	9745	1622911074584
1624002831851	Remove	1622737005753	Watermelon	Details	t	9745	1622911074584
\.


--
-- Data for Name: loggedinusers; Type: TABLE DATA; Schema: public; Owner: mvp
--

COPY public.loggedinusers (token, user_id) FROM stdin;
sha256$kP6oTWl4$c1478e13f3a001fce0bf1ddf2f43c52ebcc07d8a74b2a15f0c1bb0d8064ed02f	1625062406786100000
sha256$3tbqFjPm$2a2705c814ea9ad5e937f07407264f398572ab0b4421b0673c562ea58a0d3853	1625062406786100000
sha256$YSz1l9oP$6a5c4b799a12f1f99e2955c66c31ec0a5710ab3b2ccadbdbf46e5b899422730a	1625062406786100000
sha256$fRuzT4J9$4e7d7c8cb2360c372c97bf4fdc33320694bbd8501a20238745a8a0a15cb2e209	1625062406786100000
sha256$YcSdMZeA$5091ff62db817f286adbdc290a9073315c71bdea8a2704a067139fec9f93a9e0	1625062406786100000
sha256$tlQh3mRc$4a617c5c2347d560a530447ad72a8aab5e34fba365c66f0a0287ca79afd96528	1625062406786100000
sha256$sGwmkXRm$a98cddf1365d5a273d5ed17efa4ed19b8c549aa5a537cb5467e3df60bdcaef8f	1625062406786100000
sha256$zJWrvjmn$896980021c5ac8294a7f8818278f4b178f7f79fce8f3afa093ced28cf5b1217c	1625062406786100000
sha256$bU3Vrb9m$a2d5f40ca9df00c3009bd26e722ba7599993c482e82ee187ad61f6b2e224b001	1625062406786100000
sha256$LQVYtPb8$5b00071746e4915ab452d32a0dbc0b78d6b23bf7448f090729b8dffd74e4d839	1625062406786100000
sha256$1uwMeTY2$a78e0b025e95b6461521d2ecddba2e2781f650fc6d193799fe819e13a1dc0251	1625062406786100000
sha256$4JyCzDMR$bd0bd12afe95bdf2f88ac0121d958e6996fd1ced0d4c42de0690df867b0befb8	1625062406786100000
sha256$TOU8EZWb$11e0a8ddadfb2572320fe694d736eab3857033a7893308aa8d4d181d6265c993	1625062406786100000
sha256$qQWDeR5q$5e7ddd873feedbbd1f3440e17952269a69ebc46f7976eb8f038bd24ccdb47d6e	1625305602467790000
sha256$xKOd4Rp5$2e420d0ade41c3cd55c64e00b0844f83af871655dd20a8015e4aa982a4495187	1625062406786100000
sha256$Dm5h3Icz$5e93918050faedf834a812328d683be38f0c7d53c2374306c5af988726980e00	1625305602467790000
sha256$hsG9fnim$11d1bc65845a37f8f543b180e52ea4cdb1d7254e26b88fdaf953cfe7a340d391	1625305602467790000
sha256$647d7AsY$65c5a8df42dd7d8128a197f1bb8b7861e1a5970fc8a4a34c4a7dc7e9573895c9	1625062406786100000
sha256$zEmFXIDh$69788cab345c032fb712ee94acf536841c7b053948be2112e651fb50e2bcffb9	1625062406786100000
sha256$opCLrHly$5cd5eadb069215a3614f0e09522ee4b6d270637c933360a36087398a09f9843b	1625305602467790000
sha256$QEZf8ODG$ceda45d6ea487d1ca43977478b14b3df159b265ab520cd8b0f48d1f37b4464fc	1625062406786100000
sha256$4MpOGUJG$18587a9f5d3b950985b6aba4c2815e7c690399b074792f704ab3b3865bb48b27	1625062406786100000
sha256$tBomn3V2$aa4ae06cd2d45053c34a59ede39924ba41cbd86780cc39fc6924b536d7c313ad	1625062406786100000
\.


--
-- Data for Name: user_1623064154309668000; Type: TABLE DATA; Schema: public; Owner: mvp
--

COPY public.user_1623064154309668000 (transaction_id, transaction_type, item_id, title, details, important, arb_order, "timestamp") FROM stdin;
1622736919300	Add	1622736919298	Bread	Details	f	8965	1622736919298
1622736922568	Add	1622736922568	Banana	Details	f	85654	1622736922568
1622736988619	Add	1622736988618	Canopy	Details	f	85103	1622736988618
1622737005753	Add	1622737005753	Watermelon	Details	f	9745	1622737005753
1622737259992	Modify	1622736988618	Canopy	Details	t	85103	1622737259990
1622737355702	Modify	1622736922568	Banana	Details	t	85654	1622737355700
1622737478588	Modify	1622736922568	Banana	Details	f	85654	1622737478587
1622737479482	Modify	1622736922568	Banana	Details	t	85654	1622737479482
1622737532745	Remove	1622736988618	Canopy	Details	t	85103	1622737259990
1622737547584	Add	1622737547583	Hello	Details	f	26955	1622737547583
1622737962524	Modify	1622737547583	Hello	Details	t	26955	1622737962523
1622738014877	Modify	1622737005753	Watermelon	Details	t	9745	1622738014877
1622738059688	Add	1622738059687	Clicky	Details	f	68277	1622738059687
1622738086997	Add	1622738086997	A	Details	f	21624	1622738086997
1622738089459	Add	1622738089459	B	Details	f	86704	1622738089459
1622738091343	Modify	1622738086997	A	Details	t	21624	1622738091343
1622738969733	Remove	1622737547583	Hello	Details	t	26955	1622737962523
1622876845444	Add	1622876845442	Big	Details	f	58542	1622876845442
1622876965221	Add	1622876965221	Samsung	Details	f	51851	1622876965221
1622876992205	Add	1622876992205	Bag	Details	f	62182	1622876992205
1622877003669	Modify	1622876965221	Samsung	Details	t	51851	1622877003668
1622877007189	Modify	1622876992205	Bag	Details	t	62182	1622877007189
1622877008110	Modify	1622876992205	Bag	Details	f	62182	1622877008109
1622877008738	Modify	1622876992205	Bag	Details	t	62182	1622877008738
1622877009402	Modify	1622876992205	Bag	Details	f	62182	1622877009402
1622877010418	Modify	1622876992205	Bag	Details	t	62182	1622877010417
1622877012088	Modify	1622876992205	Bag	Details	f	62182	1622877012088
1622877275526	Modify	1622738089459	B	Details	t	86704	1622877275525
1622877333730	Modify	1622738059687	Clicky	Details	t	68277	1622877333730
1622877875998	Add	1622877875998	Trick	details	f	0	1622877875998
1622877891761	Modify	1622877875998	Trick	details	t	0	1622877891761
1622877893662	Modify	1622877875998	Trick	details	f	0	1622877893662
1622877894809	Modify	1622877875998	Trick	details	t	0	1622877894809
1622877895449	Modify	1622877875998	Trick	details	f	0	1622877895449
1622877897507	Modify	1622876992205	Bag	Details	t	62182	1622877897505
1622877898468	Modify	1622876992205	Bag	Details	f	62182	1622877898468
1622909692645	Modify	1622738089459	B	Details	f	86704	1622909692644
1622909693650	Modify	1622738089459	B	Details	t	86704	1622909693650
1622910101472	Modify	1622737005753	Watermelon	Details	f	9745	1622910101472
1622910102077	Modify	1622737005753	Watermelon	Details	t	9745	1622910102077
1622910138957	Remove	1622738059687	Clicky	Details	t	68277	1622877333730
1622910197186	Add	1622910197185	Biscuit	details	f	0	1622910197185
1622910213254	Remove	1622876992205	Bag	Details	f	62182	1622877898468
1622910216851	Remove	1622876965221	Samsung	Details	t	51851	1622877003668
1622910218324	Remove	1622876845442	Big	Details	f	58542	1622876845442
1622910241012	Add	1622910241012	Almond	details	f	0	1622910241012
1622910348088	Remove	1622738086997	A	Details	t	21624	1622738091343
1622910351242	Remove	1622738089459	B	Details	t	86704	1622909693650
1622910382882	Modify	1622910197185	Biscuit	details	t	0	1622910382882
1622910383396	Modify	1622910197185	Biscuit	details	f	0	1622910383396
1622911073898	Modify	1622737005753	Watermelon	Details	f	9745	1622911073898
1622911074584	Modify	1622737005753	Watermelon	Details	t	9745	1622911074584
1623042131553	Modify	1622910197185	Biscuit	details	t	0	1623042131553
1623042136617	Modify	1622910197185	Biscuit	details	f	0	1623042136617
1623042139089	Remove	1622877875998	Trick	details	f	0	1622877895449
1624002999069	Remove	1622737005753	Watermelon	Details	t	9745	1622911074584
\.


--
-- Data for Name: user_1624005566093007000; Type: TABLE DATA; Schema: public; Owner: mvp
--

COPY public.user_1624005566093007000 (transaction_id, transaction_type, item_id, title, details, important, arb_order, "timestamp") FROM stdin;
1624016473619	Add	1624016473617	Banana	Details	f	3565	1624016473617
1624016484161	Add	1624016484161	First!	Details	f	75475	1624016484161
\.


--
-- Data for Name: user_1625062406786100000; Type: TABLE DATA; Schema: public; Owner: mvp
--

COPY public.user_1625062406786100000 (transaction_id, transaction_type, item_id, title, details, important, arb_order, "timestamp") FROM stdin;
1625080709703	Add	1625080709703	Android	details	f	0	1625080709703
1625080740011	Add	1625080740011	Bottled Water	details	f	0	1625080740011
1625080744021	Modify	1625080740011	Bottled Water	details	t	0	1625080744021
1625081376352	Add	1625081376352	Donur	details	f	0	1625081376352
1625081386057	Modify	1625080740011	Bottled Water	details	f	0	1625081386057
1625081386789	Modify	1625080740011	Bottled Water	details	t	0	1625081386789
1625081833240	Modify	1625080709703	Android	details	t	0	1625081833240
1625081923941	Modify	1625080709703	Android	details	f	0	1625081923941
1625082140694	Modify	1625080709703	Android	details	t	0	1625082140694
1625082367814	Modify	1625080740011	Bottled Water	details	f	0	1625082367814
1625082462248	Modify	1625080740011	Bottled Water	details	t	0	1625082462248
1625082490539	Modify	1625080709703	Android	details	f	0	1625082490539
1625082610748	Modify	1625081376352	Donur	details	t	0	1625082610748
1625083275265	Modify	1625080740011	Bottled Water	details	f	0	1625083275265
1625083442699	Modify	1625080740011	Bottled Water	details	t	0	1625083442699
1625083444140	Modify	1625080740011	Bottled Water	details	f	0	1625083444140
1625083445749	Modify	1625080709703	Android	details	t	0	1625083445749
1625083446862	Modify	1625080709703	Android	details	f	0	1625083446862
1625115458236	Modify	1625080709703	Android	details	t	0	1625115458236
1625115459662	Modify	1625080709703	Android	details	f	0	1625115459662
1625115462542	Modify	1625080709703	Android	details	t	0	1625115462542
1625116706638	Modify	1625080709703	Android	details	f	0	1625116706638
1625116708684	Modify	1625080709703	Android	details	t	0	1625116708684
1625116720395	Modify	1625080709703	Android	details	f	0	1625116720395
1625116726009	Modify	1625080709703	Android	details	t	0	1625116726009
1625117478452	Modify	1625080709703	Android	details	f	0	1625117478452
1625117482886	Modify	1625080709703	Android	details	t	0	1625117482886
1625117520066	Add	1625117520066	Chocolate	details	f	0	1625117520066
1625117873528	Modify	1625080740011	Bottled Water	details	t	0	1625117873528
1625199421290	Modify	1625080740011	Bottled Water	details	f	0	1625199421290
1625199463264	Modify	1625080740011	Bottled Water	details	t	0	1625199463264
1625199501751	Modify	1625080709703	Android	details	f	0	1625199501751
1625199506069	Modify	1625117520066	Chocolate	details	t	0	1625199506069
1625199507038	Modify	1625117520066	Chocolate	details	f	0	1625199507038
1625199979704	Modify	1625080709703	Android	details	t	0	1625199979704
1625199981753	Modify	1625080709703	Android	details	f	0	1625199981753
1625200017824	Modify	1625080709703	Android	details	t	0	1625200017824
1625200022265	Modify	1625080709703	Android	details	f	0	1625200022265
1625200059593	Modify	1625080709703	Android	details	t	0	1625200059593
1625200064071	Modify	1625080709703	Android	details	f	0	1625200064071
1625200067261	Modify	1625081376352	Donur	details	f	0	1625200067261
1625200108745	Modify	1625080709703	Android	details	t	0	1625200108745
1625200111969	Modify	1625080709703	Android	details	f	0	1625200111969
1625200135615	Modify	1625080709703	Android	details	t	0	1625200135615
1625200252683	Modify	1625081376352	Donur	details	t	0	1625200252683
1625202332961	Modify	1625081376352	Donur	details	f	0	1625202332961
1625202461979	Modify	1625081376352	Donur	details	t	0	1625202461979
1625202462886	Modify	1625081376352	Donur	details	f	0	1625202462886
1625202507718	Modify	1625080709703	Android	details	f	0	1625202507718
1625202509562	Remove	1625080709703	Android	details	f	0	1625202507718
1625225394781	Modify	1625080740011	Bottled Water	details	f	0	1625225394781
1625225396075	Modify	1625081376352	Donur	details	t	0	1625225396075
1625298165429	Modify	1625081376352	Donur	details	f	0	1625298165428
1625298172615	Modify	1625080740011	Bottled Water	details	t	0	1625298172615
1625298254738	Modify	1625081376352	Donur	details	t	0	1625298254738
1625298264188	Remove	1625081376352	Donur	details	t	0	1625298254738
1625299062913	Add	1625299062913	Yesterday	details	f	0	1625299062913
1625299072694	Add	1625299072693	Salad	Details	f	30103	1625299072693
1625299072694	Add	1625299072693	Salad	Details	f	30103	1625299072693
1625301238171	Remove	1625299072693	Salad	Details	f	30103	1625299072693
1625320187237	Modify	1625299062913	Yesterday	details	t	0	1625320187235
1625320211768	Remove	1625299072693	Salad	Details	f	30103	1625299072693
1625320266425	Modify	1625080740011	Bottled Water	details	f	0	1625320266423
1625320267058	Modify	1625080740011	Bottled Water	details	t	0	1625320267058
1625320310410	Add	1625320310409	Chips	Details	f	45676	1625320310409
1625321146213	Modify	1625117520066	Chocolate	details	t	0	1625321146213
1625385629834	Modify	1625117520066	Chocolate	details	f	0	1625385629832
1625385636117	Remove	1625299062913	Yesterday	details	t	0	1625320187235
1625390187776	Modify	1625117520066	Chocolate	details	t	0	1625390187776
1625390188326	Modify	1625117520066	Chocolate	details	f	0	1625390188326
1625390200465	Modify	1625117520066	Chocolate	details	t	0	1625390200465
1625390201050	Modify	1625117520066	Chocolate	details	f	0	1625390201050
1625390223706	Modify	1625320310409	Chips	Details	t	45676	1625390223706
1625390239121	Add	1625390239121	Hero	details	f	0	1625390239121
1625467010117	Modify	1625320310409	Chips	Details	f	45676	1625467010117
1625542299840	Modify	1625117520066	Chocolate	details	t	0	1625542299840
1625565982558	Modify	1625320310409	Chips	Details	t	45676	1625565982558
1625565983152	Modify	1625320310409	Chips	Details	f	45676	1625565983152
1625639204583	Modify	1625117520066	Chocolate	details	f	0	1625639204582
1625642044637	Modify	1625320310409	Chips	Details	t	45676	1625642044635
1625642045147	Modify	1625320310409	Chips	Details	f	45676	1625642045146
\.


--
-- Data for Name: user_1625067036221060000; Type: TABLE DATA; Schema: public; Owner: mvp
--

COPY public.user_1625067036221060000 (transaction_id, transaction_type, item_id, title, details, important, arb_order, "timestamp") FROM stdin;
\.


--
-- Data for Name: user_1625079515986807000; Type: TABLE DATA; Schema: public; Owner: mvp
--

COPY public.user_1625079515986807000 (transaction_id, transaction_type, item_id, title, details, important, arb_order, "timestamp") FROM stdin;
\.


--
-- Data for Name: user_1625305455770794000; Type: TABLE DATA; Schema: public; Owner: mvp
--

COPY public.user_1625305455770794000 (transaction_id, transaction_type, item_id, title, details, important, arb_order, "timestamp") FROM stdin;
1625305466185	Add	1625305466183	Dog	Details	f	40890	1625305466183
\.


--
-- Data for Name: user_1625305602467790000; Type: TABLE DATA; Schema: public; Owner: mvp
--

COPY public.user_1625305602467790000 (transaction_id, transaction_type, item_id, title, details, important, arb_order, "timestamp") FROM stdin;
1625305613396	Add	1625305613393	Nokia	Details	f	27201	1625305613393
1625305656072	Modify	1625305613393	Nokia	Details	t	27201	1625305656072
1625306001228	Modify	1625305613393	Nokia	Details	f	27201	1625306001227
1625306007795	Modify	1625305613393	Nokia	Details	t	27201	1625306007794
1625306008658	Modify	1625305613393	Nokia	Details	f	27201	1625306008658
1625317648851	Modify	1625305613393	Nokia	Details	t	27201	1625317648851
1625564896137	Add	1625564896137	Sony	details	f	0	1625564896137
1625597817055	Remove	1625305613393	Nokia	Details	t	27201	1625317648851
1625639219242	Add	1625639219242		details	f	0	1625639219242
1625639222380	Remove	1625639219242		details	f	0	1625639219242
1625639254386	Add	1625639254386	Lens	details	f	0	1625639254386
1625639256423	Modify	1625564896137	Sony	details	t	0	1625639256423
1625639257063	Modify	1625564896137	Sony	details	f	0	1625639257063
1625639259145	Modify	1625639254386	Lens	details	t	0	1625639259145
1625639259753	Modify	1625639254386	Lens	details	f	0	1625639259753
\.


--
-- Data for Name: user_empty_table; Type: TABLE DATA; Schema: public; Owner: mvp
--

COPY public.user_empty_table (transaction_id, transaction_type, item_id, title, details, important, arb_order, "timestamp") FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: mvp
--

COPY public.users (user_id, email, pass_hash, profile) FROM stdin;
1623064154309668000	mamad@javad.com	sha256$X6t4IotB$f5699e509bef2acb88b184a423def8747a3dfd01303d073bdd1229065a70b802	Jafang
1624005566093007000	testing@example.com	sha256$H3mKOnax$347b0393040bc704a14eebc2859571b8eb505ea9785ad3cd6920a38e82d7a353	Newbe
1625062406786100000	abc@example.com	sha256$BQuaesIn$6190a077634dfbf906bd9885f0af5caf0dce08c6f79a96928bf6b10485c0f829	Newbe
1625067036221060000	abc@yahoo.com	sha256$7FYyENMb$f243172853dc5a01c0d4aacaff5b80b5439e06b78518aa97f886b9ff4feabc6e	Student
1625079515986807000	abc@order.com	sha256$ERTAn9nw$4a2efdb638bf84be9b6375cdb9e277c8f2ec397ca741e521613a4fc148402820	Engineer
1625305455770794000	Private	sha256$V0UcpdaF$72df84082cd222740b794e573a82e8912bfb32674aa4b105ba1d1dfaef72d4d2	
1625305602467790000	shrnemati@yahoo.com	sha256$bN3N9W5G$bb33fe078c40c5c86e87997b575e1ecc1526a5088a6bd68fda53ebdbfeb2554c	Private
\.


--
-- Name: item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mvp
--

SELECT pg_catalog.setval('public.item_id_seq', 55, true);


SET default_tablespace = '';

--
-- Name: items items_pkey; Type: CONSTRAINT; Schema: public; Owner: mvp
--

ALTER TABLE ONLY public.items
    ADD CONSTRAINT items_pkey PRIMARY KEY (transaction_id);


SET default_tablespace = listappdevspace;

--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: mvp; Tablespace: listappdevspace
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: mvp; Tablespace: listappdevspace
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: loggedinusers loggedinusers_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: mvp
--

ALTER TABLE ONLY public.loggedinusers
    ADD CONSTRAINT loggedinusers_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

