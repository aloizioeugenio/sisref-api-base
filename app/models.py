from django.db import models

# class Tabcargo(models.Model):
#     cod_cargo = models.CharField(db_column='COD_CARGO', primary_key=True, max_length=6)  # Field name made lowercase.
#     desc_cargo = models.CharField(db_column='DESC_CARGO', max_length=42)  # Field name made lowercase.
#     permite_banco = models.CharField(db_column='PERMITE_BANCO', max_length=3)  # Field name made lowercase.
#     subsidios = models.CharField(db_column='SUBSIDIOS', max_length=4)  # Field name made lowercase.
#     registro_siape = models.CharField(max_length=12)
#     registro_data = models.DateTimeField(blank=True, null=True)
#     nivel_cargo = models.CharField(db_column='NIVEL_CARGO', max_length=2)  # Field name made lowercase.
#     carreira = models.CharField(db_column='CARREIRA', max_length=50)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tabcargo'

class Servativ(models.Model):
    mat_siape = models.CharField(primary_key=True, max_length=7)
    mat_siapecad = models.CharField(max_length=8, blank=True, null=True)
    ident_unica = models.CharField(max_length=9)
    mat_dtp = models.CharField(max_length=7, blank=True, null=True)
    cod_serv = models.CharField(max_length=11, blank=True, null=True)
    nome_serv = models.CharField(max_length=60, blank=True, null=True)
    dt_nasc = models.DateField(blank=True, null=True)
    defvis = models.CharField(max_length=1)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    pis_pasep = models.CharField(max_length=11, blank=True, null=True)
    cod_sitcad = models.CharField(max_length=2, blank=True, null=True)
    excluido = models.CharField(max_length=1, blank=True, null=True)
    sigregjur = models.CharField(max_length=3, blank=True, null=True)
    reg_jur_at = models.CharField(max_length=1, blank=True, null=True)
    f_ing_org = models.CharField(max_length=5, blank=True, null=True)
    dt_adm = models.DateField(blank=True, null=True)
    dipl_inss = models.CharField(max_length=2, blank=True, null=True)
    n_sip_inss = models.CharField(max_length=9, blank=True, null=True)
    dt_dip_ins = models.DateField(blank=True, null=True)
    num_cargo = models.CharField(max_length=6, blank=True, null=True)
    cod_cargo = models.CharField(max_length=6, blank=True, null=True)
    dt_ing_car = models.DateField(blank=True, null=True)
    f_ing_car = models.CharField(max_length=5, blank=True, null=True)
    dipl_car = models.CharField(max_length=2, blank=True, null=True)
    n_sip_car = models.CharField(max_length=9, blank=True, null=True)
    dt_dip_car = models.DateField(blank=True, null=True)
    nivel = models.CharField(max_length=2, blank=True, null=True)
    cod_classe = models.CharField(max_length=1, blank=True, null=True)
    cod_padrao = models.CharField(max_length=3, blank=True, null=True)
    field_lot_oficial = models.CharField(db_column='_lot_oficial', max_length=10, blank=True, null=True)  # Field renamed because it started with '_'.
    cod_lot = models.CharField(max_length=8, blank=True, null=True)
    cod_uorg = models.CharField(max_length=9, blank=True, null=True)
    cod_uorg_ant = models.CharField(max_length=9, blank=True, null=True)
    cod_loc = models.CharField(max_length=8, blank=True, null=True)
    dt_ing_lot = models.DateField(blank=True, null=True)
    dt_ing_loc = models.DateField(blank=True, null=True)
    cod_lot_ant = models.CharField(max_length=9, blank=True, null=True)
    cod_loc_ant = models.CharField(max_length=8, blank=True, null=True)
    dt_sai_lot = models.DateField(blank=True, null=True)
    dt_sai_loc = models.DateField(blank=True, null=True)
    nfunc = models.CharField(max_length=5, blank=True, null=True)
    chefia = models.CharField(max_length=1, blank=True, null=True)
    area = models.CharField(max_length=1, blank=True, null=True)
    jornada = models.CharField(max_length=2, blank=True, null=True)
    dt_ing_jorn = models.DateField(blank=True, null=True)
    jornada_aps12h = models.CharField(max_length=2)
    dt_ing_jorn_aps12h = models.DateField(blank=True, null=True)
    entra_trab = models.TimeField(blank=True, null=True)
    ini_interv = models.TimeField(blank=True, null=True)
    sai_interv = models.TimeField(blank=True, null=True)
    sai_trab = models.TimeField(blank=True, null=True)
    horae = models.CharField(max_length=1, blank=True, null=True)
    processo = models.CharField(max_length=20, blank=True, null=True)
    motivo = models.CharField(max_length=1, blank=True, null=True)
    dthe = models.DateField(blank=True, null=True)
    dthefim = models.DateField(blank=True, null=True)
    malt = models.CharField(max_length=2, blank=True, null=True)
    autchef = models.CharField(max_length=1, blank=True, null=True)
    bhoras = models.CharField(max_length=1, blank=True, null=True)
    bh_tipo = models.CharField(max_length=1, blank=True, null=True)
    dt_ini_int = models.DateField(blank=True, null=True)
    reg_obito_dt = models.DateField(blank=True, null=True)
    oco_exclu_oco = models.CharField(max_length=5, blank=True, null=True)
    oco_exclu_dt = models.DateField(blank=True, null=True)
    oco_exclu_dl_cod = models.CharField(max_length=2, blank=True, null=True)
    oco_exclu_dl_num = models.CharField(max_length=12, blank=True, null=True)
    oco_exclu_dl_dt_publ = models.DateField(blank=True, null=True)
    idrecad = models.CharField(max_length=1, blank=True, null=True)
    freqh = models.CharField(max_length=1, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    motidev = models.TextField(blank=True, null=True)
    sexo = models.CharField(max_length=1)
    identificacao_apelido = models.CharField(max_length=40)
    mae = models.CharField(max_length=60)
    pai = models.CharField(max_length=60)
    tipo_sanguineo = models.CharField(max_length=3)
    jornada_cargo = models.CharField(max_length=2)
    nome_social = models.CharField(max_length=60, blank=True, null=True)
    flag_nome_social = models.IntegerField(blank=True, null=True)
    isencao_ponto = models.IntegerField()
    limite_horas = models.CharField(max_length=3)
    plantao_medico = models.CharField(max_length=3)
    acesso_biometrico = models.CharField(max_length=1)
    # id = models.AutoField()
    dt_atualizacao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'servativ'
        unique_together = (('mat_siape', 'ident_unica'),)

class Tabsetor(models.Model):
    codigo = models.CharField(primary_key=True, max_length=8)
    descricao = models.CharField(max_length=110, blank=True, null=True)
    tb0700 = models.CharField(max_length=8, blank=True, null=True)
    uorg_anterior = models.CharField(max_length=9, blank=True, null=True)
    cod_uorg = models.CharField(max_length=9)
    area = models.CharField(max_length=1, blank=True, null=True)
    cod_uorg_pai = models.CharField(max_length=9, blank=True, null=True)
    uorg_pai = models.CharField(max_length=8, blank=True, null=True)
    upag = models.CharField(max_length=9, blank=True, null=True)
    ug = models.CharField(max_length=6, blank=True, null=True)
    inicio_atend = models.TimeField(blank=True, null=True)
    fim_atend = models.TimeField(blank=True, null=True)
    sigla = models.CharField(max_length=12, blank=True, null=True)
    tfreq = models.CharField(max_length=1, blank=True, null=True)
    dfreq = models.CharField(max_length=1)
    ativo = models.CharField(max_length=1)
    end_lota = models.TextField(blank=True, null=True)
    num_lota = models.CharField(max_length=10, blank=True, null=True)
    bairro_lota = models.CharField(max_length=50, blank=True, null=True)
    cidade_lota = models.CharField(max_length=50, blank=True, null=True)
    cep_lota = models.CharField(max_length=8, blank=True, null=True)
    tel_lota = models.CharField(max_length=8, blank=True, null=True)
    uf_lota = models.CharField(max_length=2, blank=True, null=True)
    codmun = models.CharField(max_length=6, blank=True, null=True)
    regiao = models.CharField(max_length=3, blank=True, null=True)
    regional = models.CharField(max_length=1, blank=True, null=True)
    fuso_horario = models.FloatField()
    horario_verao = models.CharField(max_length=1)
    liberar_homologacao = models.DateField(blank=True, null=True)
    acessou_sistema_supervisao = models.DateTimeField(blank=True, null=True)
    manter_turno_estendido_de = models.DateTimeField(blank=True, null=True)
    manter_turno_estendido_ate = models.DateTimeField(blank=True, null=True)
    suspender_turno_estendido_de = models.DateTimeField(blank=True, null=True)
    suspender_turno_estendido_ate = models.DateTimeField(blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)
    data_desativacao = models.DateField(blank=True, null=True)
    restrito_horario_atend = models.CharField(max_length=1)
    periodo_excecao = models.CharField(max_length=3, blank=True, null=True)
    acesso_biometrico = models.CharField(max_length=1)
    # id = models.AutoField()
    depara = models.CharField(max_length=8, blank=True, null=True)
    gerencia = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'tabsetor'
