PGDMP  -    9        	    	    |            embarque_2024    13.16    16.4     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    25251    embarque_2024    DATABASE     �   CREATE DATABASE embarque_2024 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE embarque_2024;
                postgres    false                        2615    25410    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                postgres    false            �            1259    25411    _prisma_migrations    TABLE     �  CREATE TABLE public._prisma_migrations (
    id character varying(36) NOT NULL,
    checksum character varying(64) NOT NULL,
    finished_at timestamp with time zone,
    migration_name character varying(255) NOT NULL,
    logs text,
    rolled_back_at timestamp with time zone,
    started_at timestamp with time zone DEFAULT now() NOT NULL,
    applied_steps_count integer DEFAULT 0 NOT NULL
);
 &   DROP TABLE public._prisma_migrations;
       public         heap    postgres    false    5            �            1259    25485    reports    TABLE       CREATE TABLE public.reports (
    id integer NOT NULL,
    type_document text NOT NULL,
    name_document text NOT NULL,
    label text NOT NULL,
    inital_value text NOT NULL,
    final_value text NOT NULL,
    edit boolean NOT NULL,
    is_null boolean NOT NULL
);
    DROP TABLE public.reports;
       public         heap    postgres    false    5            �            1259    25483    reports_id_seq    SEQUENCE     �   CREATE SEQUENCE public.reports_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.reports_id_seq;
       public          postgres    false    202    5            �           0    0    reports_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.reports_id_seq OWNED BY public.reports.id;
          public          postgres    false    201            *           2604    25488 
   reports id    DEFAULT     h   ALTER TABLE ONLY public.reports ALTER COLUMN id SET DEFAULT nextval('public.reports_id_seq'::regclass);
 9   ALTER TABLE public.reports ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    201    202    202            �          0    25411    _prisma_migrations 
   TABLE DATA           �   COPY public._prisma_migrations (id, checksum, finished_at, migration_name, logs, rolled_back_at, started_at, applied_steps_count) FROM stdin;
    public          postgres    false    200          �          0    25485    reports 
   TABLE DATA           t   COPY public.reports (id, type_document, name_document, label, inital_value, final_value, edit, is_null) FROM stdin;
    public          postgres    false    202   K       �           0    0    reports_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.reports_id_seq', 93, true);
          public          postgres    false    201            ,           2606    25420 *   _prisma_migrations _prisma_migrations_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public._prisma_migrations
    ADD CONSTRAINT _prisma_migrations_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public._prisma_migrations DROP CONSTRAINT _prisma_migrations_pkey;
       public            postgres    false    200            .           2606    25493    reports reports_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.reports
    ADD CONSTRAINT reports_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.reports DROP CONSTRAINT reports_pkey;
       public            postgres    false    202            �   (  x���ɍ[1�_Q8
�/
b"0�z�!;�_��`x���_���6ݻf���"��T�P�̔%�r@Xז,�����"�Q0�T	�'���7n��<lo�|��  )��M�&|U#�(��_HE���������q�8�Q%�g/	�p�^j�\�<�<��4w`$�8�X5��j���g���)�u���:��
&���NA7�kb(ț 1�_��>4dk��P�F�4Yr���������*�i��
Pk��]�x2��c5�]o�jsK�3�=^M�����Wt�|�߯���/���      �   �  x��Y�n��V����@���W�]F��ؒ!�)vQ@��t��re;-���w}�>ȾX�c{-�R㠀#�(~G3�ᐱ���U�,��Y5�˙Xm�Y1��g�U���bYn6U���5�4fڞې����ir�����a�%qD���È��/����e���EYL�J����pF��!F#��.9��/5s�Ίm���Ŭ�t���1zgPjk[m{c�Z-��j�Q+?����Y��o�e1�j�9��{L��ӔI��x�7�#��B�v.o�a���
4f�;B\�AAS��m5��s���<�2��R�������̖~3�W�m]l@��XM+�9@�ڙm_�����Ƙ���3��Q��X��lL�#�w��uQ6�%q��d}�L�ǈ|��$��S���N:�W�wKQW����f-� �k���H����6�k'I�0�BS��r��+���c��Z����H����F�o:!�����>�\��V3�;��1��"��&x7���`y�!�nB���zG9̦� GƾF�\�P��n��oX=��?"�mb0�W�f
߸ڂ�;��ǘMq^wLO��1!�I��,��'�H�&:�<Gg��[��c�fz�&�yy��i��O<�8�F��B ��a�������~���8�q����]���Fq�+~L�Q��1O4��I'�8LI,�t��H�TSk�G��)����~�jF.�,�6�|�X��Ѧ�(���Э��E,�`|"A�O�~	��<|�����܂1������;d��ɰ?9&	���� ��Q<�潛�!@ �n�����ؾ��|�]6H6���5��d&ȯ��k%�B��!k����C���	2�<R���k�VZې���;�si1/Ģ Y�x+VW���E��[�R���k�&�b*`�a3L�ؖ��Ϙ���e{�wl�0HD���8�c���<013l�aQ9�L9�b�������x�NMWhӗ��Ռ�N��X�n3[g�+�R��VW3�y*���Q<�pH�Q�Ɇ�d q��h���w�1��1�&�G�_�&�h�g��0�%@�q2L�lWu�C[�l��2_U�B+�P��Sd1�/[� [`e��y��! H����ҴXLw���L�֦'Ajy����u-6[i	�k{9����}��-�8�з���ۺ�>]a��̔�_CF[�H��^�s���P.��;�ݳ������.�y��4hҏ�v��:��sՁ��w2�rD��B��;��VLC�(6�
V���i(����g�-W�>�gP���l��J�з����.�<��8yN�\�����ߠ �TӲX����l������A���~4Rd�QclZ����M��v�SY���N�޾��V����~��FKnt��:�����Q�R4��c<{D���d�r�+�?�`��3F�V墨˂�(`Q�Wc��p��a�y������W��R�P�+9k�L����ՙ#zˢ\t́9��Z�i���E�ӧղ�QR���mޝ��?����\� �ԯU}�)�.&Ԁ,U�"�8.WG+-w�<��M��Gu�rt�Ϙ ��z�,;�I���fbE<��w��G�TLRؖ�O�f\��9D^�)�.��W�����Cjᓧd<�~�#�%��F��EF��p�a��AruZ�]}ܒGO�^6��%ʑ��p@���zт!����9�KQ�\uf�0�j&�����	{�q��ڼ����]]�}H��x��=5��b!��Jt)�c"��y�3!�\4 ��Aڦ�O0�>A2�6�sр�jԼ��͉��8�ܢ������r�n��w��y�u]���{��<'��֨�ߨ/�K�$i?���$ �{5�T�5��+�ž��H�]M�,������Տ��8�����ơ��"��cQ��@�c��V��c��1��X��C�!'�~�GgW��#	kiD��xC:�j�����V�����~�;j�1�9M�����s���1aS`ўm�a;�G<����z��wԑ��޻^[Ʃ��h{�xEJ������B��]�& U���N��Z�Y��`4|�-d�0��>{�+~��\���%�3��0�A�F�r��v�؟��K���(9�$3�f0��m[#��M����F�Z     