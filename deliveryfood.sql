PGDMP                         w            DeliveryFood    12.0    12.0 b    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16703    DeliveryFood    DATABASE     �   CREATE DATABASE "DeliveryFood" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Russian_Russia.1251' LC_CTYPE = 'Russian_Russia.1251';
    DROP DATABASE "DeliveryFood";
                postgres    false            �           0    0    DATABASE "DeliveryFood"    ACL     5   GRANT CONNECT ON DATABASE "DeliveryFood" TO "Vasya";
                   postgres    false    2998            �            1259    16823    category_of_dishes    TABLE     �   CREATE TABLE public.category_of_dishes (
    "ID_category_dishes" integer NOT NULL,
    "Name_category_dishes" character varying(255)
);
 &   DROP TABLE public.category_of_dishes;
       public         heap    postgres    false            �            1259    16793    clients    TABLE     �   CREATE TABLE public.clients (
    "ID_client" integer NOT NULL,
    "Name_client" character varying(255),
    "Address_client" character varying(255),
    "Comment_client" text,
    "Phone_client" character varying(12)
);
    DROP TABLE public.clients;
       public         heap    postgres    false            �            1259    16724    courier_service    TABLE     �   CREATE TABLE public.courier_service (
    "ID_courier_service" integer NOT NULL,
    "Name_courier_service" character varying(255),
    "Address_main_office" character varying(255),
    "INN" character varying(15),
    "Phone" character varying(12)
);
 #   DROP TABLE public.courier_service;
       public         heap    postgres    false            �            1259    16704    couriers    TABLE     �  CREATE TABLE public.couriers (
    "ID_courier" integer NOT NULL,
    "ID_courier_service" integer,
    "ID_type_courier" integer,
    "ID_status_courier" integer,
    "Surname" character varying(255),
    "Name" character varying(255),
    "Second_name" character varying(255),
    "Phone" character varying(12),
    "Birthday" date,
    "Passport" bigint,
    "Date_activation" date,
    "Bank_account" numeric(20,0)
);
    DROP TABLE public.couriers;
       public         heap    postgres    false            �            1259    16788 
   deliveries    TABLE     �   CREATE TABLE public.deliveries (
    "ID_delivery" integer NOT NULL,
    "ID_courier" integer,
    "ID_client" integer,
    "Date_delivery" date,
    "ID_order" integer
);
    DROP TABLE public.deliveries;
       public         heap    postgres    false            �            1259    16828    dishes    TABLE     �   CREATE TABLE public.dishes (
    "ID_dish" integer NOT NULL,
    id_restaurant integer,
    "ID_category_of_dishes" integer,
    name_dish character varying(255),
    "Prize_dish" money
);
    DROP TABLE public.dishes;
       public         heap    postgres    false            �            1259    16813    dishes_in_order    TABLE     z   CREATE TABLE public.dishes_in_order (
    "Number_dishes" integer NOT NULL,
    "ID_order" integer,
    "Dish" integer
);
 #   DROP TABLE public.dishes_in_order;
       public         heap    postgres    false            �            1259    16798    orders    TABLE     �   CREATE TABLE public.orders (
    "ID_order" integer NOT NULL,
    "ID_type_payments" integer,
    "ID_status" integer,
    "Deliver_in" time(6) without time zone,
    "ID_restaurant" integer,
    "ID_client" integer,
    "ID_discount" integer
);
    DROP TABLE public.orders;
       public         heap    postgres    false            �            1259    16863    passport_date    TABLE     	  CREATE TABLE public.passport_date (
    "Serial/Number" bigint NOT NULL,
    "Place_of_birth" character varying(255),
    "Issued_by_whom" character varying(255),
    "When_issued" date,
    "Unit_code" integer,
    "Address_registration" character varying(255)
);
 !   DROP TABLE public.passport_date;
       public         heap    postgres    false            �            1259    16868 	   positions    TABLE     �   CREATE TABLE public.positions (
    "ID_position" integer NOT NULL,
    "Name_position" character varying(255),
    "Salary_position" numeric(8,0)
);
    DROP TABLE public.positions;
       public         heap    postgres    false            �            1259    16873 
   requisites    TABLE     �   CREATE TABLE public.requisites (
    "Number_account" numeric(20,0) NOT NULL,
    "BIK" character varying(9),
    "INN" character varying(15),
    "KPP" character varying(9)
);
    DROP TABLE public.requisites;
       public         heap    postgres    false            �            1259    16833 
   restaurant    TABLE       CREATE TABLE public.restaurant (
    id_restaurant integer NOT NULL,
    name_restaurant character varying(255),
    "ID_underground" integer,
    "Address_restaurant" character varying(255),
    "Comment_restaurant" text,
    "Phone_restaurant" character varying(12)
);
    DROP TABLE public.restaurant;
       public         heap    postgres    false            �           0    0    TABLE restaurant    ACL     6   GRANT SELECT ON TABLE public.restaurant TO "Clients";
          public          postgres    false    215            �            1259    16848    shifts    TABLE     �   CREATE TABLE public.shifts (
    "ID_shift" integer NOT NULL,
    "Date_shift" date,
    "Time_start_shift" time(6) without time zone,
    "Time_end_shift" time(6) without time zone
);
    DROP TABLE public.shifts;
       public         heap    postgres    false            �            1259    16843    slots    TABLE     �   CREATE TABLE public.slots (
    "ID_slot" integer NOT NULL,
    "ID_shift" integer,
    "ID_courier" integer,
    "ID_underground" integer
);
    DROP TABLE public.slots;
       public         heap    postgres    false            �            1259    16709    status_courier    TABLE     s   CREATE TABLE public.status_courier (
    "ID_status" integer NOT NULL,
    "Name_status" character varying(255)
);
 "   DROP TABLE public.status_courier;
       public         heap    postgres    false            �            1259    16803    status_order    TABLE     |   CREATE TABLE public.status_order (
    "ID_status_order" integer NOT NULL,
    "Name_status_order" character varying(20)
);
     DROP TABLE public.status_order;
       public         heap    postgres    false            �            1259    16808    system_discount    TABLE     �   CREATE TABLE public.system_discount (
    "ID_discount" integer NOT NULL,
    "Name_discount" character varying(255),
    "Percent_discount" integer,
    "PROMOKOD" character varying(10)
);
 #   DROP TABLE public.system_discount;
       public         heap    postgres    false            �            1259    16719    type_courier    TABLE     m   CREATE TABLE public.type_courier (
    "ID_type" integer NOT NULL,
    "Name_type" character varying(255)
);
     DROP TABLE public.type_courier;
       public         heap    postgres    false            �            1259    16818    type_payments    TABLE        CREATE TABLE public.type_payments (
    "ID_type_payments" integer NOT NULL,
    "Name_type_payments" character varying(20)
);
 !   DROP TABLE public.type_payments;
       public         heap    postgres    false            �            1259    16838    underground    TABLE     z   CREATE TABLE public.underground (
    "ID_underground" integer NOT NULL,
    "Name_underground" character varying(255)
);
    DROP TABLE public.underground;
       public         heap    postgres    false            �            1259    16858    workers    TABLE     t  CREATE TABLE public.workers (
    "ID_worker" integer NOT NULL,
    "Position_worker" integer,
    "Surname_worker" character varying(255),
    "Name_worker" character varying(255),
    "Second_name_worker" character varying(255),
    "Passport_worker" bigint,
    "Birthday_worker" date,
    "Phone_worker" character varying(12),
    "Requisites_worker" numeric(20,0)
);
    DROP TABLE public.workers;
       public         heap    postgres    false            �            1259    16853    workers_on_shift    TABLE     v   CREATE TABLE public.workers_on_shift (
    "Number" integer NOT NULL,
    "ID_shift" integer,
    "Worker" integer
);
 $   DROP TABLE public.workers_on_shift;
       public         heap    postgres    false            �          0    16823    category_of_dishes 
   TABLE DATA           Z   COPY public.category_of_dishes ("ID_category_dishes", "Name_category_dishes") FROM stdin;
    public          postgres    false    213   ��       �          0    16793    clients 
   TABLE DATA           q   COPY public.clients ("ID_client", "Name_client", "Address_client", "Comment_client", "Phone_client") FROM stdin;
    public          postgres    false    207   ��       �          0    16724    courier_service 
   TABLE DATA           ~   COPY public.courier_service ("ID_courier_service", "Name_courier_service", "Address_main_office", "INN", "Phone") FROM stdin;
    public          postgres    false    205   ?�       �          0    16704    couriers 
   TABLE DATA           �   COPY public.couriers ("ID_courier", "ID_courier_service", "ID_type_courier", "ID_status_courier", "Surname", "Name", "Second_name", "Phone", "Birthday", "Passport", "Date_activation", "Bank_account") FROM stdin;
    public          postgres    false    202   i�       �          0    16788 
   deliveries 
   TABLE DATA           k   COPY public.deliveries ("ID_delivery", "ID_courier", "ID_client", "Date_delivery", "ID_order") FROM stdin;
    public          postgres    false    206   ҆       �          0    16828    dishes 
   TABLE DATA           l   COPY public.dishes ("ID_dish", id_restaurant, "ID_category_of_dishes", name_dish, "Prize_dish") FROM stdin;
    public          postgres    false    214   "�       �          0    16813    dishes_in_order 
   TABLE DATA           N   COPY public.dishes_in_order ("Number_dishes", "ID_order", "Dish") FROM stdin;
    public          postgres    false    211   ��       �          0    16798    orders 
   TABLE DATA           �   COPY public.orders ("ID_order", "ID_type_payments", "ID_status", "Deliver_in", "ID_restaurant", "ID_client", "ID_discount") FROM stdin;
    public          postgres    false    208   �       �          0    16863    passport_date 
   TABLE DATA           �   COPY public.passport_date ("Serial/Number", "Place_of_birth", "Issued_by_whom", "When_issued", "Unit_code", "Address_registration") FROM stdin;
    public          postgres    false    221   I�       �          0    16868 	   positions 
   TABLE DATA           V   COPY public.positions ("ID_position", "Name_position", "Salary_position") FROM stdin;
    public          postgres    false    222   B�       �          0    16873 
   requisites 
   TABLE DATA           K   COPY public.requisites ("Number_account", "BIK", "INN", "KPP") FROM stdin;
    public          postgres    false    223   ��       �          0    16833 
   restaurant 
   TABLE DATA           �   COPY public.restaurant (id_restaurant, name_restaurant, "ID_underground", "Address_restaurant", "Comment_restaurant", "Phone_restaurant") FROM stdin;
    public          postgres    false    215   �       �          0    16848    shifts 
   TABLE DATA           `   COPY public.shifts ("ID_shift", "Date_shift", "Time_start_shift", "Time_end_shift") FROM stdin;
    public          postgres    false    218   @�       �          0    16843    slots 
   TABLE DATA           V   COPY public.slots ("ID_slot", "ID_shift", "ID_courier", "ID_underground") FROM stdin;
    public          postgres    false    217   ��       �          0    16709    status_courier 
   TABLE DATA           D   COPY public.status_courier ("ID_status", "Name_status") FROM stdin;
    public          postgres    false    203   :�       �          0    16803    status_order 
   TABLE DATA           N   COPY public.status_order ("ID_status_order", "Name_status_order") FROM stdin;
    public          postgres    false    209   x�       �          0    16808    system_discount 
   TABLE DATA           i   COPY public.system_discount ("ID_discount", "Name_discount", "Percent_discount", "PROMOKOD") FROM stdin;
    public          postgres    false    210   ֑       �          0    16719    type_courier 
   TABLE DATA           >   COPY public.type_courier ("ID_type", "Name_type") FROM stdin;
    public          postgres    false    204   ��       �          0    16818    type_payments 
   TABLE DATA           Q   COPY public.type_payments ("ID_type_payments", "Name_type_payments") FROM stdin;
    public          postgres    false    212   ݒ       �          0    16838    underground 
   TABLE DATA           K   COPY public.underground ("ID_underground", "Name_underground") FROM stdin;
    public          postgres    false    216   #�       �          0    16858    workers 
   TABLE DATA           �   COPY public.workers ("ID_worker", "Position_worker", "Surname_worker", "Name_worker", "Second_name_worker", "Passport_worker", "Birthday_worker", "Phone_worker", "Requisites_worker") FROM stdin;
    public          postgres    false    220   ��       �          0    16853    workers_on_shift 
   TABLE DATA           J   COPY public.workers_on_shift ("Number", "ID_shift", "Worker") FROM stdin;
    public          postgres    false    219   �       �
           2606    16827 *   category_of_dishes Category_of_dishes_pkey 
   CONSTRAINT     |   ALTER TABLE ONLY public.category_of_dishes
    ADD CONSTRAINT "Category_of_dishes_pkey" PRIMARY KEY ("ID_category_dishes");
 V   ALTER TABLE ONLY public.category_of_dishes DROP CONSTRAINT "Category_of_dishes_pkey";
       public            postgres    false    213            �
           2606    16797    clients Clients_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.clients
    ADD CONSTRAINT "Clients_pkey" PRIMARY KEY ("ID_client");
 @   ALTER TABLE ONLY public.clients DROP CONSTRAINT "Clients_pkey";
       public            postgres    false    207            �
           2606    16728 $   courier_service Courier_service_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.courier_service
    ADD CONSTRAINT "Courier_service_pkey" PRIMARY KEY ("ID_courier_service");
 P   ALTER TABLE ONLY public.courier_service DROP CONSTRAINT "Courier_service_pkey";
       public            postgres    false    205            �
           2606    16708    couriers Couriers_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.couriers
    ADD CONSTRAINT "Couriers_pkey" PRIMARY KEY ("ID_courier");
 B   ALTER TABLE ONLY public.couriers DROP CONSTRAINT "Couriers_pkey";
       public            postgres    false    202            �
           2606    16792    deliveries Deliveries_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.deliveries
    ADD CONSTRAINT "Deliveries_pkey" PRIMARY KEY ("ID_delivery");
 F   ALTER TABLE ONLY public.deliveries DROP CONSTRAINT "Deliveries_pkey";
       public            postgres    false    206            �
           2606    16817 $   dishes_in_order Dishes_in_order_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY public.dishes_in_order
    ADD CONSTRAINT "Dishes_in_order_pkey" PRIMARY KEY ("Number_dishes");
 P   ALTER TABLE ONLY public.dishes_in_order DROP CONSTRAINT "Dishes_in_order_pkey";
       public            postgres    false    211            �
           2606    16832    dishes Dishes_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.dishes
    ADD CONSTRAINT "Dishes_pkey" PRIMARY KEY ("ID_dish");
 >   ALTER TABLE ONLY public.dishes DROP CONSTRAINT "Dishes_pkey";
       public            postgres    false    214            �
           2606    16802    orders Orders_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT "Orders_pkey" PRIMARY KEY ("ID_order");
 >   ALTER TABLE ONLY public.orders DROP CONSTRAINT "Orders_pkey";
       public            postgres    false    208            �
           2606    17240     passport_date Passport_date_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public.passport_date
    ADD CONSTRAINT "Passport_date_pkey" PRIMARY KEY ("Serial/Number");
 L   ALTER TABLE ONLY public.passport_date DROP CONSTRAINT "Passport_date_pkey";
       public            postgres    false    221                        2606    16872    positions Positions_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.positions
    ADD CONSTRAINT "Positions_pkey" PRIMARY KEY ("ID_position");
 D   ALTER TABLE ONLY public.positions DROP CONSTRAINT "Positions_pkey";
       public            postgres    false    222                       2606    17290    requisites Requisites_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.requisites
    ADD CONSTRAINT "Requisites_pkey" PRIMARY KEY ("Number_account");
 F   ALTER TABLE ONLY public.requisites DROP CONSTRAINT "Requisites_pkey";
       public            postgres    false    223            �
           2606    16837    restaurant Restaurant_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.restaurant
    ADD CONSTRAINT "Restaurant_pkey" PRIMARY KEY (id_restaurant);
 F   ALTER TABLE ONLY public.restaurant DROP CONSTRAINT "Restaurant_pkey";
       public            postgres    false    215            �
           2606    16852    shifts Shifts_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.shifts
    ADD CONSTRAINT "Shifts_pkey" PRIMARY KEY ("ID_shift");
 >   ALTER TABLE ONLY public.shifts DROP CONSTRAINT "Shifts_pkey";
       public            postgres    false    218            �
           2606    16847    slots Slots_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.slots
    ADD CONSTRAINT "Slots_pkey" PRIMARY KEY ("ID_slot");
 <   ALTER TABLE ONLY public.slots DROP CONSTRAINT "Slots_pkey";
       public            postgres    false    217            �
           2606    16713 "   status_courier Status_courier_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.status_courier
    ADD CONSTRAINT "Status_courier_pkey" PRIMARY KEY ("ID_status");
 N   ALTER TABLE ONLY public.status_courier DROP CONSTRAINT "Status_courier_pkey";
       public            postgres    false    203            �
           2606    16807    status_order Status_order_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public.status_order
    ADD CONSTRAINT "Status_order_pkey" PRIMARY KEY ("ID_status_order");
 J   ALTER TABLE ONLY public.status_order DROP CONSTRAINT "Status_order_pkey";
       public            postgres    false    209            �
           2606    16812 $   system_discount System_discount_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY public.system_discount
    ADD CONSTRAINT "System_discount_pkey" PRIMARY KEY ("ID_discount");
 P   ALTER TABLE ONLY public.system_discount DROP CONSTRAINT "System_discount_pkey";
       public            postgres    false    210            �
           2606    16723    type_courier Type_courier_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.type_courier
    ADD CONSTRAINT "Type_courier_pkey" PRIMARY KEY ("ID_type");
 J   ALTER TABLE ONLY public.type_courier DROP CONSTRAINT "Type_courier_pkey";
       public            postgres    false    204            �
           2606    16822     type_payments Type_payments_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.type_payments
    ADD CONSTRAINT "Type_payments_pkey" PRIMARY KEY ("ID_type_payments");
 L   ALTER TABLE ONLY public.type_payments DROP CONSTRAINT "Type_payments_pkey";
       public            postgres    false    212            �
           2606    16842    underground Underground_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.underground
    ADD CONSTRAINT "Underground_pkey" PRIMARY KEY ("ID_underground");
 H   ALTER TABLE ONLY public.underground DROP CONSTRAINT "Underground_pkey";
       public            postgres    false    216            �
           2606    16857 &   workers_on_shift Workers_on_shift_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.workers_on_shift
    ADD CONSTRAINT "Workers_on_shift_pkey" PRIMARY KEY ("Number");
 R   ALTER TABLE ONLY public.workers_on_shift DROP CONSTRAINT "Workers_on_shift_pkey";
       public            postgres    false    219            �
           2606    16862    workers Workers_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.workers
    ADD CONSTRAINT "Workers_pkey" PRIMARY KEY ("ID_worker");
 @   ALTER TABLE ONLY public.workers DROP CONSTRAINT "Workers_pkey";
       public            postgres    false    220                       2606    17305 #   couriers Couriers_Bank_account_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.couriers
    ADD CONSTRAINT "Couriers_Bank_account_fkey" FOREIGN KEY ("Bank_account") REFERENCES public.requisites("Number_account") NOT VALID;
 O   ALTER TABLE ONLY public.couriers DROP CONSTRAINT "Couriers_Bank_account_fkey";
       public          postgres    false    2818    223    202                       2606    16979 )   couriers Couriers_ID_courier_service_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.couriers
    ADD CONSTRAINT "Couriers_ID_courier_service_fkey" FOREIGN KEY ("ID_courier_service") REFERENCES public.courier_service("ID_courier_service") NOT VALID;
 U   ALTER TABLE ONLY public.couriers DROP CONSTRAINT "Couriers_ID_courier_service_fkey";
       public          postgres    false    202    2782    205                       2606    16714 (   couriers Couriers_ID_status_courier_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.couriers
    ADD CONSTRAINT "Couriers_ID_status_courier_fkey" FOREIGN KEY ("ID_status_courier") REFERENCES public.status_courier("ID_status") NOT VALID;
 T   ALTER TABLE ONLY public.couriers DROP CONSTRAINT "Couriers_ID_status_courier_fkey";
       public          postgres    false    2778    203    202                       2606    16974 &   couriers Couriers_ID_type_courier_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.couriers
    ADD CONSTRAINT "Couriers_ID_type_courier_fkey" FOREIGN KEY ("ID_type_courier") REFERENCES public.type_courier("ID_type") NOT VALID;
 R   ALTER TABLE ONLY public.couriers DROP CONSTRAINT "Couriers_ID_type_courier_fkey";
       public          postgres    false    2780    204    202                       2606    17455    couriers Couriers_Passport_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.couriers
    ADD CONSTRAINT "Couriers_Passport_fkey" FOREIGN KEY ("Passport") REFERENCES public.passport_date("Serial/Number") NOT VALID;
 K   ALTER TABLE ONLY public.couriers DROP CONSTRAINT "Couriers_Passport_fkey";
       public          postgres    false    202    221    2814            
           2606    17097 $   deliveries Deliveries_ID_client_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.deliveries
    ADD CONSTRAINT "Deliveries_ID_client_fkey" FOREIGN KEY ("ID_client") REFERENCES public.clients("ID_client") NOT VALID;
 P   ALTER TABLE ONLY public.deliveries DROP CONSTRAINT "Deliveries_ID_client_fkey";
       public          postgres    false    207    206    2786            	           2606    17092 %   deliveries Deliveries_ID_courier_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.deliveries
    ADD CONSTRAINT "Deliveries_ID_courier_fkey" FOREIGN KEY ("ID_courier") REFERENCES public.couriers("ID_courier") NOT VALID;
 Q   ALTER TABLE ONLY public.deliveries DROP CONSTRAINT "Deliveries_ID_courier_fkey";
       public          postgres    false    2776    202    206                       2606    17087 #   deliveries Deliveries_ID_order_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.deliveries
    ADD CONSTRAINT "Deliveries_ID_order_fkey" FOREIGN KEY ("ID_order") REFERENCES public.orders("ID_order") NOT VALID;
 O   ALTER TABLE ONLY public.deliveries DROP CONSTRAINT "Deliveries_ID_order_fkey";
       public          postgres    false    206    2788    208                       2606    17112 (   dishes Dishes_ID_category_of_dishes_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.dishes
    ADD CONSTRAINT "Dishes_ID_category_of_dishes_fkey" FOREIGN KEY ("ID_category_of_dishes") REFERENCES public.category_of_dishes("ID_category_dishes") NOT VALID;
 T   ALTER TABLE ONLY public.dishes DROP CONSTRAINT "Dishes_ID_category_of_dishes_fkey";
       public          postgres    false    213    214    2798                       2606    17117     dishes Dishes_ID_restaurant_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.dishes
    ADD CONSTRAINT "Dishes_ID_restaurant_fkey" FOREIGN KEY (id_restaurant) REFERENCES public.restaurant(id_restaurant) NOT VALID;
 L   ALTER TABLE ONLY public.dishes DROP CONSTRAINT "Dishes_ID_restaurant_fkey";
       public          postgres    false    2802    215    214                       2606    17127 )   dishes_in_order Dishes_in_order_Dish_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.dishes_in_order
    ADD CONSTRAINT "Dishes_in_order_Dish_fkey" FOREIGN KEY ("Dish") REFERENCES public.dishes("ID_dish") NOT VALID;
 U   ALTER TABLE ONLY public.dishes_in_order DROP CONSTRAINT "Dishes_in_order_Dish_fkey";
       public          postgres    false    214    211    2800                       2606    17122 -   dishes_in_order Dishes_in_order_ID_order_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.dishes_in_order
    ADD CONSTRAINT "Dishes_in_order_ID_order_fkey" FOREIGN KEY ("ID_order") REFERENCES public.orders("ID_order") NOT VALID;
 Y   ALTER TABLE ONLY public.dishes_in_order DROP CONSTRAINT "Dishes_in_order_ID_order_fkey";
       public          postgres    false    2788    211    208                       2606    17102    orders Orders_ID_client_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT "Orders_ID_client_fkey" FOREIGN KEY ("ID_client") REFERENCES public.clients("ID_client") NOT VALID;
 H   ALTER TABLE ONLY public.orders DROP CONSTRAINT "Orders_ID_client_fkey";
       public          postgres    false    207    208    2786                       2606    17077    orders Orders_ID_discount_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT "Orders_ID_discount_fkey" FOREIGN KEY ("ID_discount") REFERENCES public.system_discount("ID_discount") NOT VALID;
 J   ALTER TABLE ONLY public.orders DROP CONSTRAINT "Orders_ID_discount_fkey";
       public          postgres    false    2792    210    208                       2606    17107     orders Orders_ID_restaurant_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT "Orders_ID_restaurant_fkey" FOREIGN KEY ("ID_restaurant") REFERENCES public.restaurant(id_restaurant) NOT VALID;
 L   ALTER TABLE ONLY public.orders DROP CONSTRAINT "Orders_ID_restaurant_fkey";
       public          postgres    false    2802    215    208                       2606    17082    orders Orders_ID_status_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT "Orders_ID_status_fkey" FOREIGN KEY ("ID_status") REFERENCES public.status_order("ID_status_order") NOT VALID;
 H   ALTER TABLE ONLY public.orders DROP CONSTRAINT "Orders_ID_status_fkey";
       public          postgres    false    2790    209    208                       2606    17072 #   orders Orders_ID_type_payments_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT "Orders_ID_type_payments_fkey" FOREIGN KEY ("ID_type_payments") REFERENCES public.type_payments("ID_type_payments") NOT VALID;
 O   ALTER TABLE ONLY public.orders DROP CONSTRAINT "Orders_ID_type_payments_fkey";
       public          postgres    false    208    2796    212                       2606    17067 )   restaurant Restaurant_ID_underground_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.restaurant
    ADD CONSTRAINT "Restaurant_ID_underground_fkey" FOREIGN KEY ("ID_underground") REFERENCES public.underground("ID_underground") NOT VALID;
 U   ALTER TABLE ONLY public.restaurant DROP CONSTRAINT "Restaurant_ID_underground_fkey";
       public          postgres    false    216    215    2804                       2606    17057    slots Slots_ID_courier_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.slots
    ADD CONSTRAINT "Slots_ID_courier_fkey" FOREIGN KEY ("ID_courier") REFERENCES public.couriers("ID_courier") NOT VALID;
 G   ALTER TABLE ONLY public.slots DROP CONSTRAINT "Slots_ID_courier_fkey";
       public          postgres    false    217    202    2776                       2606    17052    slots Slots_ID_shift_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.slots
    ADD CONSTRAINT "Slots_ID_shift_fkey" FOREIGN KEY ("ID_shift") REFERENCES public.shifts("ID_shift") NOT VALID;
 E   ALTER TABLE ONLY public.slots DROP CONSTRAINT "Slots_ID_shift_fkey";
       public          postgres    false    218    2808    217                       2606    17062    slots Slots_ID_underground_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.slots
    ADD CONSTRAINT "Slots_ID_underground_fkey" FOREIGN KEY ("ID_underground") REFERENCES public.underground("ID_underground") NOT VALID;
 K   ALTER TABLE ONLY public.slots DROP CONSTRAINT "Slots_ID_underground_fkey";
       public          postgres    false    2804    217    216                       2606    17415 $   workers Workers_Passport_worker_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.workers
    ADD CONSTRAINT "Workers_Passport_worker_fkey" FOREIGN KEY ("Passport_worker") REFERENCES public.passport_date("Serial/Number") NOT VALID;
 P   ALTER TABLE ONLY public.workers DROP CONSTRAINT "Workers_Passport_worker_fkey";
       public          postgres    false    220    2814    221                       2606    17027 $   workers Workers_Position_worker_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.workers
    ADD CONSTRAINT "Workers_Position_worker_fkey" FOREIGN KEY ("Position_worker") REFERENCES public.positions("ID_position") NOT VALID;
 P   ALTER TABLE ONLY public.workers DROP CONSTRAINT "Workers_Position_worker_fkey";
       public          postgres    false    220    222    2816                       2606    17314 &   workers Workers_Requisites_worker_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.workers
    ADD CONSTRAINT "Workers_Requisites_worker_fkey" FOREIGN KEY ("Requisites_worker") REFERENCES public.requisites("Number_account") NOT VALID;
 R   ALTER TABLE ONLY public.workers DROP CONSTRAINT "Workers_Requisites_worker_fkey";
       public          postgres    false    2818    220    223                       2606    17042 /   workers_on_shift Workers_on_shift_ID_shift_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.workers_on_shift
    ADD CONSTRAINT "Workers_on_shift_ID_shift_fkey" FOREIGN KEY ("ID_shift") REFERENCES public.shifts("ID_shift") NOT VALID;
 [   ALTER TABLE ONLY public.workers_on_shift DROP CONSTRAINT "Workers_on_shift_ID_shift_fkey";
       public          postgres    false    219    218    2808                       2606    17047 -   workers_on_shift Workers_on_shift_Worker_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.workers_on_shift
    ADD CONSTRAINT "Workers_on_shift_Worker_fkey" FOREIGN KEY ("Worker") REFERENCES public.workers("ID_worker") NOT VALID;
 Y   ALTER TABLE ONLY public.workers_on_shift DROP CONSTRAINT "Workers_on_shift_Worker_fkey";
       public          postgres    false    2812    219    220            �   _   x����0��b�x��c�ЁK��^G�J�M-ܙt�9�h�'#oF��
7�fV]���� ���l8��@g��𰶘�1V >�q7r      �   6  x�m�AN�0D��),u	�;Nj��ahR��B���i��mz��[b��V���g\��]����-��L�}���:L��ޠ�Th��g�u������X�<&�s,yt
�kВъ���E�[+��'|��� �$�w9�e�YƖ/�)L�~-Z��g���5��ʱqVr�+-:n�	j8�����,<�U|RQ�xc�,�teKk\5�}�/R���?�z�Q���mD����ym�BKj,�f�?�2��bp���aŨ}���1�;����-e�����F�Wbw���6=��R#W��ɸ�)���:�R� >1
�      �     x�U��JAE��_1{%������FĿ���F�D�GpнQ��p���CE���Z�:�*�st�{���1�A�[,��|����v����l�|�6����$��Tb�W[щ�0��j�p�9Z|⊵��<�bC�暣�l��MA|0�I)���`�Uh������\��G��y����z�,*��D�lp1����H[	�i�C�0�=�x�0� ʽ�K[�h,-I>�lr���+!i�Nq��^����l<���re��2Jr�2ܰ�#W��{���o��      �   Y  x�]�MJ�1���*��d�s	O�ô�Ѕ�AA�Z�Z�j�g���I�-J �O�<y'4�>��6�O���7�G���^����e��w��[թ]�I�X���TzbO	b�ĔS-�H�c����K-y<C�/��q�~�>��������吝��kF+B���1{\.)彜�m�Xj��!�U��\��{�nFP�|��vm�k�w}�_���b\9t7y$O�*K�a���v5�k��h�r��EW?�È6Y�m7�vn��1�G�
�ht�j�}o9[��X�CZN��E�z���v^' fr�vm���ͱ��#�ʸ͡���v�f�~��]"1������N�s�H�      �   @   x�M��	�0Cѳ�KBe[�����s(������=C1���������,��{�O�3I�5      �   V  x��TKnZA\�@����=`���0�-'���đ"9���q�������BύR==3B��X]՟�nF+���������M۴�-=�����RiS�*������/~@S��Ti+��i2�A�)�΀��`)�kԪ�;�z��E`��6�B��.�D]�XObc���s_�7�U\��m?�����t���s��c�����\Eka\��5�ӌu�-���H1B�ʳ��4���*q��j�R�I���<�o�ڡ�%VMr)���&�R�X��<Q��[O�]a<@�6ִD՜��sw�G*�X�!B>���B��rQ.�	�״natC���6*�n���XaMPgF[U����/�]��#'k3��k�1_)6���䪕`�}�Y^W�cW3���?�l���|��o����{�<�	�4Mo�d��d����5��gUƸ���������SN�ajd��G��e��V�;V�8�)��v;�=��xJ:A��/7�%�Ӟl�?A�xu�2�=����qx���;XSzq
p_t0=AN+(��TE%�H�.�Sg����K(ۈ2��Ĺ#��W�/�����8��L���'�V��jf      �   \   x���ABѳ0�®���:�8_xB(I:�rN�s�"���3��L��r��&R;Q�U��AӦ�j��m�~���r��E��y��k}      �   E   x�%���0�0L����!:A�����Nba�hJq��.�B"Y�>�����X�M�SOƬ����� f�      �   �  x��Umr�0��`�;0����K��;�ıS�m��f2���Ut��{�c��;��Ǿ����R�R.��C���o��7~�?��_�5>[_�{������}�w�M>�"%�L�&2V��㒷��FJ�k�\w�>�A}���;▙���E���T��e�z�/!�%��v���,�2�����q�F�U���?�V~�2O�MS*�[s�����>0#o��W s���
 ˾�=�3�n�M�x�UZ��h�c�[�x�6\�x��9��'���-�VԢ�jaxT�GJ�B�3�/�bM���-M�i��g�.��"��	�}%�t*\*ETJ1~�i0!zm1�r�!�PN#�Z�BY� �!P�(Q����|�H��t�a��������0D�����V=J�^6;ɨGӏp,���0	U�l䬀�� M�X��~qr�ƫAJb����&�@H)bm��ym�؎۷���6	u��o���ؓV;�x"�+�<�w/�A�Ȼ������_�"���v�u�1��%����W9�C&/=)Ra"����*KX�u�,��ݑFHX�X�O���`�����k�8[`�gv�c��?8m��؛4�e�Ğ]���8q"UJo=�t6|�+j��m����p�c��@�1V�U�ZNd�0��ɉW�z�-��AW�/*sc�������,&���x�S���|�ђ�X+Un��m�a	L)��h3���.����:�s      �   o   x����@D�����16C� x�/؁��Zx�#���L���Uh�бi�Jdδf��>3v6��^+�f������m��_�����'�/[��ZkS��)..ιi�@P      �     x�5Q�q 1{�b2`�^�����m@��NZV�_˘Z����t�����F
��od��v۬�N��۸�Uxn�4�xd�Tz�]�>S`�Z'y�!C
��*T�z��e��>br6{�`ޝ��v;i0�.��+؜K���a����_��f|P��'_8�;Z�N�a��b*nJU�+���'���X��F���0�`��
�:L��V�� �c�h���;�D��H�փ:�EgJ��~�EL���y�:!��H?ȹ��7$BflXT���7�������9�?�?��p
      �   B  x����j�@��w�b�[��$&y���?P�
��P�m���D�+�y��$��M���|g�X�J��`%#��#2yP��ʎ�F�ͳ<����c�
�H垙=r֌�<�s�_e��Ğ���)S7���y�),�r-i)�%�(2i8�ºf�q�!r�� ��9����R���] ����f�Z�Ju�N�-�g���Q�_���~m7���c�<��Y�✢V{bDg��D�W,��^�4�FL��C�>��ZF�8�����6��V���&�:��~Se[�K}��Ȭ���]�����b����껎���C      �   d   x�m�A� D�5ܥC�j�����&ň����� �z ��G�A����X	��Z�־'�c%M�yr޴��ؾ��9���iC��8�x�C���{2���B�      �   v   x�%��C1B�a���:�]���\Y2ȱO�b��>�+6�㰺8�W�{���1x0|���5�)o��l� W��B4�'�O���Ijè
���l]x).��1��̒�:���}H����      �   .   x�3�0�®�Mv\�ta녽1y\F��^تpa�8W� ���      �   N   x�m���0�q� ���"��6�V�$����3����Ń�Q91��D��5-�AK$���|oz�=z�:Hz��=r      �   �   x�U�=�@��S�	�.?��P�
��p(B�aQ�M��;��H��������8I�8�st��j�HS�q@"j`�V���-&
5�ɞC��q�8<%{�
��=D&��8$iVpD���L�Y��+�u"��T��h��Bڬ9��t��
V��GdH��,=F��3 ��G      �   =   x�3�0��֋v\��e�ya҅�v_�wa���{�R\Ɯ&\�t�	M8F��� �	%]      �   6   x�3�0��/̸��Z}a�@��@n�E\F�&^�za:~U1z\\\ �-e      �   �   x�=���@D��*\�n(��%D���º���1�d?�3;|��5�˂#��+�4u�ڸ�m8�{)��c������ċz�9�q��A�;��׶
�~)��$;Y�:Ќ�:K���2633� ��sS      �   S  x�m�AN[A��UР�g<�/�	r��!��V-(���H�"��p��N�7�~�ϿB���ɟ}�� ������~��,̟����|	ܐȺh4���'bd�]	�0e�!���밉 ����?���.��0���q�E��W����hPRK��)���ԡih<�
�{��M|S�����%W��Jt����1��%8JՂ�l���Aǈhj�����z.�~�������|�a�o�̖�&��;�$%�Z��R�aC	!�#V(�[i�n�9��5<���V{�<&8��ĕ�����R���`q6-N�i��4�k      �   �   x���@߸�h�{����Ȑ�G`# ##Uhɨ5�J�6Z:���N=��Ĕ	�� M�"���Z o�f,�����`y�*.�2���Ȋ�@m@� �����G3e^��QM�nNy'.y5�w3��H�p�!d     