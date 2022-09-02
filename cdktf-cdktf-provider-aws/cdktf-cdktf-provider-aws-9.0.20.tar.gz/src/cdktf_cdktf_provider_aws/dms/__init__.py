import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf
import constructs


class DmsCertificate(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dms.DmsCertificate",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate aws_dms_certificate}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        certificate_id: builtins.str,
        certificate_pem: typing.Optional[builtins.str] = None,
        certificate_wallet: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate aws_dms_certificate} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param certificate_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#certificate_id DmsCertificate#certificate_id}.
        :param certificate_pem: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#certificate_pem DmsCertificate#certificate_pem}.
        :param certificate_wallet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#certificate_wallet DmsCertificate#certificate_wallet}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#id DmsCertificate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#tags DmsCertificate#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#tags_all DmsCertificate#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsCertificate.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DmsCertificateConfig(
            certificate_id=certificate_id,
            certificate_pem=certificate_pem,
            certificate_wallet=certificate_wallet,
            id=id,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCertificatePem")
    def reset_certificate_pem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePem", []))

    @jsii.member(jsii_name="resetCertificateWallet")
    def reset_certificate_wallet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateWallet", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @builtins.property
    @jsii.member(jsii_name="certificateIdInput")
    def certificate_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePemInput")
    def certificate_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePemInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateWalletInput")
    def certificate_wallet_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateWalletInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateId")
    def certificate_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateId"))

    @certificate_id.setter
    def certificate_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsCertificate, "certificate_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateId", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePem")
    def certificate_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificatePem"))

    @certificate_pem.setter
    def certificate_pem(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsCertificate, "certificate_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePem", value)

    @builtins.property
    @jsii.member(jsii_name="certificateWallet")
    def certificate_wallet(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateWallet"))

    @certificate_wallet.setter
    def certificate_wallet(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsCertificate, "certificate_wallet").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateWallet", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsCertificate, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsCertificate, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsCertificate, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dms.DmsCertificateConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "certificate_id": "certificateId",
        "certificate_pem": "certificatePem",
        "certificate_wallet": "certificateWallet",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class DmsCertificateConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        certificate_id: builtins.str,
        certificate_pem: typing.Optional[builtins.str] = None,
        certificate_wallet: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS Database Migration Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param certificate_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#certificate_id DmsCertificate#certificate_id}.
        :param certificate_pem: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#certificate_pem DmsCertificate#certificate_pem}.
        :param certificate_wallet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#certificate_wallet DmsCertificate#certificate_wallet}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#id DmsCertificate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#tags DmsCertificate#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#tags_all DmsCertificate#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DmsCertificateConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument certificate_id", value=certificate_id, expected_type=type_hints["certificate_id"])
            check_type(argname="argument certificate_pem", value=certificate_pem, expected_type=type_hints["certificate_pem"])
            check_type(argname="argument certificate_wallet", value=certificate_wallet, expected_type=type_hints["certificate_wallet"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_id": certificate_id,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if certificate_pem is not None:
            self._values["certificate_pem"] = certificate_pem
        if certificate_wallet is not None:
            self._values["certificate_wallet"] = certificate_wallet
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def certificate_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#certificate_id DmsCertificate#certificate_id}.'''
        result = self._values.get("certificate_id")
        assert result is not None, "Required property 'certificate_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_pem(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#certificate_pem DmsCertificate#certificate_pem}.'''
        result = self._values.get("certificate_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_wallet(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#certificate_wallet DmsCertificate#certificate_wallet}.'''
        result = self._values.get("certificate_wallet")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#id DmsCertificate#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#tags DmsCertificate#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_certificate#tags_all DmsCertificate#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsCertificateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEndpoint(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dms.DmsEndpoint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint aws_dms_endpoint}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        endpoint_id: builtins.str,
        endpoint_type: builtins.str,
        engine_name: builtins.str,
        certificate_arn: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        elasticsearch_settings: typing.Optional[typing.Union["DmsEndpointElasticsearchSettings", typing.Dict[str, typing.Any]]] = None,
        extra_connection_attributes: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kafka_settings: typing.Optional[typing.Union["DmsEndpointKafkaSettings", typing.Dict[str, typing.Any]]] = None,
        kinesis_settings: typing.Optional[typing.Union["DmsEndpointKinesisSettings", typing.Dict[str, typing.Any]]] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        mongodb_settings: typing.Optional[typing.Union["DmsEndpointMongodbSettings", typing.Dict[str, typing.Any]]] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        redshift_settings: typing.Optional[typing.Union["DmsEndpointRedshiftSettings", typing.Dict[str, typing.Any]]] = None,
        s3_settings: typing.Optional[typing.Union["DmsEndpointS3Settings", typing.Dict[str, typing.Any]]] = None,
        secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
        secrets_manager_arn: typing.Optional[builtins.str] = None,
        server_name: typing.Optional[builtins.str] = None,
        service_access_role: typing.Optional[builtins.str] = None,
        ssl_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DmsEndpointTimeouts", typing.Dict[str, typing.Any]]] = None,
        username: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint aws_dms_endpoint} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_id DmsEndpoint#endpoint_id}.
        :param endpoint_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_type DmsEndpoint#endpoint_type}.
        :param engine_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#engine_name DmsEndpoint#engine_name}.
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#certificate_arn DmsEndpoint#certificate_arn}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#database_name DmsEndpoint#database_name}.
        :param elasticsearch_settings: elasticsearch_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#elasticsearch_settings DmsEndpoint#elasticsearch_settings}
        :param extra_connection_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#extra_connection_attributes DmsEndpoint#extra_connection_attributes}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#id DmsEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kafka_settings: kafka_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kafka_settings DmsEndpoint#kafka_settings}
        :param kinesis_settings: kinesis_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kinesis_settings DmsEndpoint#kinesis_settings}
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kms_key_arn DmsEndpoint#kms_key_arn}.
        :param mongodb_settings: mongodb_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#mongodb_settings DmsEndpoint#mongodb_settings}
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#password DmsEndpoint#password}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#port DmsEndpoint#port}.
        :param redshift_settings: redshift_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#redshift_settings DmsEndpoint#redshift_settings}
        :param s3_settings: s3_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#s3_settings DmsEndpoint#s3_settings}
        :param secrets_manager_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#secrets_manager_access_role_arn DmsEndpoint#secrets_manager_access_role_arn}.
        :param secrets_manager_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#secrets_manager_arn DmsEndpoint#secrets_manager_arn}.
        :param server_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_name DmsEndpoint#server_name}.
        :param service_access_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role DmsEndpoint#service_access_role}.
        :param ssl_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_mode DmsEndpoint#ssl_mode}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#tags DmsEndpoint#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#tags_all DmsEndpoint#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#timeouts DmsEndpoint#timeouts}
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#username DmsEndpoint#username}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEndpoint.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DmsEndpointConfig(
            endpoint_id=endpoint_id,
            endpoint_type=endpoint_type,
            engine_name=engine_name,
            certificate_arn=certificate_arn,
            database_name=database_name,
            elasticsearch_settings=elasticsearch_settings,
            extra_connection_attributes=extra_connection_attributes,
            id=id,
            kafka_settings=kafka_settings,
            kinesis_settings=kinesis_settings,
            kms_key_arn=kms_key_arn,
            mongodb_settings=mongodb_settings,
            password=password,
            port=port,
            redshift_settings=redshift_settings,
            s3_settings=s3_settings,
            secrets_manager_access_role_arn=secrets_manager_access_role_arn,
            secrets_manager_arn=secrets_manager_arn,
            server_name=server_name,
            service_access_role=service_access_role,
            ssl_mode=ssl_mode,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            username=username,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putElasticsearchSettings")
    def put_elasticsearch_settings(
        self,
        *,
        endpoint_uri: builtins.str,
        service_access_role_arn: builtins.str,
        error_retry_duration: typing.Optional[jsii.Number] = None,
        full_load_error_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param endpoint_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_uri DmsEndpoint#endpoint_uri}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.
        :param error_retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#error_retry_duration DmsEndpoint#error_retry_duration}.
        :param full_load_error_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#full_load_error_percentage DmsEndpoint#full_load_error_percentage}.
        '''
        value = DmsEndpointElasticsearchSettings(
            endpoint_uri=endpoint_uri,
            service_access_role_arn=service_access_role_arn,
            error_retry_duration=error_retry_duration,
            full_load_error_percentage=full_load_error_percentage,
        )

        return typing.cast(None, jsii.invoke(self, "putElasticsearchSettings", [value]))

    @jsii.member(jsii_name="putKafkaSettings")
    def put_kafka_settings(
        self,
        *,
        broker: builtins.str,
        include_control_details: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_null_and_empty: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_partition_value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_transaction_details: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        message_format: typing.Optional[builtins.str] = None,
        message_max_bytes: typing.Optional[jsii.Number] = None,
        no_hex_prefix: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sasl_password: typing.Optional[builtins.str] = None,
        sasl_username: typing.Optional[builtins.str] = None,
        security_protocol: typing.Optional[builtins.str] = None,
        ssl_ca_certificate_arn: typing.Optional[builtins.str] = None,
        ssl_client_certificate_arn: typing.Optional[builtins.str] = None,
        ssl_client_key_arn: typing.Optional[builtins.str] = None,
        ssl_client_key_password: typing.Optional[builtins.str] = None,
        topic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param broker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#broker DmsEndpoint#broker}.
        :param include_control_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_control_details DmsEndpoint#include_control_details}.
        :param include_null_and_empty: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_null_and_empty DmsEndpoint#include_null_and_empty}.
        :param include_partition_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_partition_value DmsEndpoint#include_partition_value}.
        :param include_table_alter_operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_table_alter_operations DmsEndpoint#include_table_alter_operations}.
        :param include_transaction_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_transaction_details DmsEndpoint#include_transaction_details}.
        :param message_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_format DmsEndpoint#message_format}.
        :param message_max_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_max_bytes DmsEndpoint#message_max_bytes}.
        :param no_hex_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#no_hex_prefix DmsEndpoint#no_hex_prefix}.
        :param partition_include_schema_table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#partition_include_schema_table DmsEndpoint#partition_include_schema_table}.
        :param sasl_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#sasl_password DmsEndpoint#sasl_password}.
        :param sasl_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#sasl_username DmsEndpoint#sasl_username}.
        :param security_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#security_protocol DmsEndpoint#security_protocol}.
        :param ssl_ca_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_ca_certificate_arn DmsEndpoint#ssl_ca_certificate_arn}.
        :param ssl_client_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_certificate_arn DmsEndpoint#ssl_client_certificate_arn}.
        :param ssl_client_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_key_arn DmsEndpoint#ssl_client_key_arn}.
        :param ssl_client_key_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_key_password DmsEndpoint#ssl_client_key_password}.
        :param topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#topic DmsEndpoint#topic}.
        '''
        value = DmsEndpointKafkaSettings(
            broker=broker,
            include_control_details=include_control_details,
            include_null_and_empty=include_null_and_empty,
            include_partition_value=include_partition_value,
            include_table_alter_operations=include_table_alter_operations,
            include_transaction_details=include_transaction_details,
            message_format=message_format,
            message_max_bytes=message_max_bytes,
            no_hex_prefix=no_hex_prefix,
            partition_include_schema_table=partition_include_schema_table,
            sasl_password=sasl_password,
            sasl_username=sasl_username,
            security_protocol=security_protocol,
            ssl_ca_certificate_arn=ssl_ca_certificate_arn,
            ssl_client_certificate_arn=ssl_client_certificate_arn,
            ssl_client_key_arn=ssl_client_key_arn,
            ssl_client_key_password=ssl_client_key_password,
            topic=topic,
        )

        return typing.cast(None, jsii.invoke(self, "putKafkaSettings", [value]))

    @jsii.member(jsii_name="putKinesisSettings")
    def put_kinesis_settings(
        self,
        *,
        include_control_details: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_null_and_empty: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_partition_value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_transaction_details: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        message_format: typing.Optional[builtins.str] = None,
        partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_access_role_arn: typing.Optional[builtins.str] = None,
        stream_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param include_control_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_control_details DmsEndpoint#include_control_details}.
        :param include_null_and_empty: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_null_and_empty DmsEndpoint#include_null_and_empty}.
        :param include_partition_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_partition_value DmsEndpoint#include_partition_value}.
        :param include_table_alter_operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_table_alter_operations DmsEndpoint#include_table_alter_operations}.
        :param include_transaction_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_transaction_details DmsEndpoint#include_transaction_details}.
        :param message_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_format DmsEndpoint#message_format}.
        :param partition_include_schema_table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#partition_include_schema_table DmsEndpoint#partition_include_schema_table}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.
        :param stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#stream_arn DmsEndpoint#stream_arn}.
        '''
        value = DmsEndpointKinesisSettings(
            include_control_details=include_control_details,
            include_null_and_empty=include_null_and_empty,
            include_partition_value=include_partition_value,
            include_table_alter_operations=include_table_alter_operations,
            include_transaction_details=include_transaction_details,
            message_format=message_format,
            partition_include_schema_table=partition_include_schema_table,
            service_access_role_arn=service_access_role_arn,
            stream_arn=stream_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisSettings", [value]))

    @jsii.member(jsii_name="putMongodbSettings")
    def put_mongodb_settings(
        self,
        *,
        auth_mechanism: typing.Optional[builtins.str] = None,
        auth_source: typing.Optional[builtins.str] = None,
        auth_type: typing.Optional[builtins.str] = None,
        docs_to_investigate: typing.Optional[builtins.str] = None,
        extract_doc_id: typing.Optional[builtins.str] = None,
        nesting_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_mechanism: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_mechanism DmsEndpoint#auth_mechanism}.
        :param auth_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_source DmsEndpoint#auth_source}.
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_type DmsEndpoint#auth_type}.
        :param docs_to_investigate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#docs_to_investigate DmsEndpoint#docs_to_investigate}.
        :param extract_doc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#extract_doc_id DmsEndpoint#extract_doc_id}.
        :param nesting_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#nesting_level DmsEndpoint#nesting_level}.
        '''
        value = DmsEndpointMongodbSettings(
            auth_mechanism=auth_mechanism,
            auth_source=auth_source,
            auth_type=auth_type,
            docs_to_investigate=docs_to_investigate,
            extract_doc_id=extract_doc_id,
            nesting_level=nesting_level,
        )

        return typing.cast(None, jsii.invoke(self, "putMongodbSettings", [value]))

    @jsii.member(jsii_name="putRedshiftSettings")
    def put_redshift_settings(
        self,
        *,
        bucket_folder: typing.Optional[builtins.str] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        encryption_mode: typing.Optional[builtins.str] = None,
        server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        service_access_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_folder DmsEndpoint#bucket_folder}.
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_name DmsEndpoint#bucket_name}.
        :param encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encryption_mode DmsEndpoint#encryption_mode}.
        :param server_side_encryption_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_side_encryption_kms_key_id DmsEndpoint#server_side_encryption_kms_key_id}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.
        '''
        value = DmsEndpointRedshiftSettings(
            bucket_folder=bucket_folder,
            bucket_name=bucket_name,
            encryption_mode=encryption_mode,
            server_side_encryption_kms_key_id=server_side_encryption_kms_key_id,
            service_access_role_arn=service_access_role_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putRedshiftSettings", [value]))

    @jsii.member(jsii_name="putS3Settings")
    def put_s3_settings(
        self,
        *,
        add_column_name: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        bucket_folder: typing.Optional[builtins.str] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        canned_acl_for_objects: typing.Optional[builtins.str] = None,
        cdc_inserts_and_updates: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cdc_inserts_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cdc_max_batch_interval: typing.Optional[jsii.Number] = None,
        cdc_min_file_size: typing.Optional[jsii.Number] = None,
        cdc_path: typing.Optional[builtins.str] = None,
        compression_type: typing.Optional[builtins.str] = None,
        csv_delimiter: typing.Optional[builtins.str] = None,
        csv_no_sup_value: typing.Optional[builtins.str] = None,
        csv_null_value: typing.Optional[builtins.str] = None,
        csv_row_delimiter: typing.Optional[builtins.str] = None,
        data_format: typing.Optional[builtins.str] = None,
        data_page_size: typing.Optional[jsii.Number] = None,
        date_partition_delimiter: typing.Optional[builtins.str] = None,
        date_partition_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        date_partition_sequence: typing.Optional[builtins.str] = None,
        dict_page_size_limit: typing.Optional[jsii.Number] = None,
        enable_statistics: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encoding_type: typing.Optional[builtins.str] = None,
        encryption_mode: typing.Optional[builtins.str] = None,
        external_table_definition: typing.Optional[builtins.str] = None,
        ignore_headers_row: typing.Optional[jsii.Number] = None,
        include_op_for_full_load: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_file_size: typing.Optional[jsii.Number] = None,
        parquet_timestamp_in_millisecond: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        parquet_version: typing.Optional[builtins.str] = None,
        preserve_transactions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rfc4180: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        row_group_length: typing.Optional[jsii.Number] = None,
        server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        service_access_role_arn: typing.Optional[builtins.str] = None,
        timestamp_column_name: typing.Optional[builtins.str] = None,
        use_csv_no_sup_value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param add_column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#add_column_name DmsEndpoint#add_column_name}.
        :param bucket_folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_folder DmsEndpoint#bucket_folder}.
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_name DmsEndpoint#bucket_name}.
        :param canned_acl_for_objects: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#canned_acl_for_objects DmsEndpoint#canned_acl_for_objects}.
        :param cdc_inserts_and_updates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_inserts_and_updates DmsEndpoint#cdc_inserts_and_updates}.
        :param cdc_inserts_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_inserts_only DmsEndpoint#cdc_inserts_only}.
        :param cdc_max_batch_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_max_batch_interval DmsEndpoint#cdc_max_batch_interval}.
        :param cdc_min_file_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_min_file_size DmsEndpoint#cdc_min_file_size}.
        :param cdc_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_path DmsEndpoint#cdc_path}.
        :param compression_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#compression_type DmsEndpoint#compression_type}.
        :param csv_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_delimiter DmsEndpoint#csv_delimiter}.
        :param csv_no_sup_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_no_sup_value DmsEndpoint#csv_no_sup_value}.
        :param csv_null_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_null_value DmsEndpoint#csv_null_value}.
        :param csv_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_row_delimiter DmsEndpoint#csv_row_delimiter}.
        :param data_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#data_format DmsEndpoint#data_format}.
        :param data_page_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#data_page_size DmsEndpoint#data_page_size}.
        :param date_partition_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_delimiter DmsEndpoint#date_partition_delimiter}.
        :param date_partition_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_enabled DmsEndpoint#date_partition_enabled}.
        :param date_partition_sequence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_sequence DmsEndpoint#date_partition_sequence}.
        :param dict_page_size_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#dict_page_size_limit DmsEndpoint#dict_page_size_limit}.
        :param enable_statistics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#enable_statistics DmsEndpoint#enable_statistics}.
        :param encoding_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encoding_type DmsEndpoint#encoding_type}.
        :param encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encryption_mode DmsEndpoint#encryption_mode}.
        :param external_table_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#external_table_definition DmsEndpoint#external_table_definition}.
        :param ignore_headers_row: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ignore_headers_row DmsEndpoint#ignore_headers_row}.
        :param include_op_for_full_load: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_op_for_full_load DmsEndpoint#include_op_for_full_load}.
        :param max_file_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#max_file_size DmsEndpoint#max_file_size}.
        :param parquet_timestamp_in_millisecond: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#parquet_timestamp_in_millisecond DmsEndpoint#parquet_timestamp_in_millisecond}.
        :param parquet_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#parquet_version DmsEndpoint#parquet_version}.
        :param preserve_transactions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#preserve_transactions DmsEndpoint#preserve_transactions}.
        :param rfc4180: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#rfc_4180 DmsEndpoint#rfc_4180}.
        :param row_group_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#row_group_length DmsEndpoint#row_group_length}.
        :param server_side_encryption_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_side_encryption_kms_key_id DmsEndpoint#server_side_encryption_kms_key_id}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.
        :param timestamp_column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#timestamp_column_name DmsEndpoint#timestamp_column_name}.
        :param use_csv_no_sup_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#use_csv_no_sup_value DmsEndpoint#use_csv_no_sup_value}.
        '''
        value = DmsEndpointS3Settings(
            add_column_name=add_column_name,
            bucket_folder=bucket_folder,
            bucket_name=bucket_name,
            canned_acl_for_objects=canned_acl_for_objects,
            cdc_inserts_and_updates=cdc_inserts_and_updates,
            cdc_inserts_only=cdc_inserts_only,
            cdc_max_batch_interval=cdc_max_batch_interval,
            cdc_min_file_size=cdc_min_file_size,
            cdc_path=cdc_path,
            compression_type=compression_type,
            csv_delimiter=csv_delimiter,
            csv_no_sup_value=csv_no_sup_value,
            csv_null_value=csv_null_value,
            csv_row_delimiter=csv_row_delimiter,
            data_format=data_format,
            data_page_size=data_page_size,
            date_partition_delimiter=date_partition_delimiter,
            date_partition_enabled=date_partition_enabled,
            date_partition_sequence=date_partition_sequence,
            dict_page_size_limit=dict_page_size_limit,
            enable_statistics=enable_statistics,
            encoding_type=encoding_type,
            encryption_mode=encryption_mode,
            external_table_definition=external_table_definition,
            ignore_headers_row=ignore_headers_row,
            include_op_for_full_load=include_op_for_full_load,
            max_file_size=max_file_size,
            parquet_timestamp_in_millisecond=parquet_timestamp_in_millisecond,
            parquet_version=parquet_version,
            preserve_transactions=preserve_transactions,
            rfc4180=rfc4180,
            row_group_length=row_group_length,
            server_side_encryption_kms_key_id=server_side_encryption_kms_key_id,
            service_access_role_arn=service_access_role_arn,
            timestamp_column_name=timestamp_column_name,
            use_csv_no_sup_value=use_csv_no_sup_value,
        )

        return typing.cast(None, jsii.invoke(self, "putS3Settings", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#create DmsEndpoint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#delete DmsEndpoint#delete}.
        '''
        value = DmsEndpointTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCertificateArn")
    def reset_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateArn", []))

    @jsii.member(jsii_name="resetDatabaseName")
    def reset_database_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseName", []))

    @jsii.member(jsii_name="resetElasticsearchSettings")
    def reset_elasticsearch_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticsearchSettings", []))

    @jsii.member(jsii_name="resetExtraConnectionAttributes")
    def reset_extra_connection_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraConnectionAttributes", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKafkaSettings")
    def reset_kafka_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKafkaSettings", []))

    @jsii.member(jsii_name="resetKinesisSettings")
    def reset_kinesis_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisSettings", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetMongodbSettings")
    def reset_mongodb_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMongodbSettings", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetRedshiftSettings")
    def reset_redshift_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedshiftSettings", []))

    @jsii.member(jsii_name="resetS3Settings")
    def reset_s3_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Settings", []))

    @jsii.member(jsii_name="resetSecretsManagerAccessRoleArn")
    def reset_secrets_manager_access_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretsManagerAccessRoleArn", []))

    @jsii.member(jsii_name="resetSecretsManagerArn")
    def reset_secrets_manager_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretsManagerArn", []))

    @jsii.member(jsii_name="resetServerName")
    def reset_server_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerName", []))

    @jsii.member(jsii_name="resetServiceAccessRole")
    def reset_service_access_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccessRole", []))

    @jsii.member(jsii_name="resetSslMode")
    def reset_ssl_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslMode", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchSettings")
    def elasticsearch_settings(
        self,
    ) -> "DmsEndpointElasticsearchSettingsOutputReference":
        return typing.cast("DmsEndpointElasticsearchSettingsOutputReference", jsii.get(self, "elasticsearchSettings"))

    @builtins.property
    @jsii.member(jsii_name="endpointArn")
    def endpoint_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointArn"))

    @builtins.property
    @jsii.member(jsii_name="kafkaSettings")
    def kafka_settings(self) -> "DmsEndpointKafkaSettingsOutputReference":
        return typing.cast("DmsEndpointKafkaSettingsOutputReference", jsii.get(self, "kafkaSettings"))

    @builtins.property
    @jsii.member(jsii_name="kinesisSettings")
    def kinesis_settings(self) -> "DmsEndpointKinesisSettingsOutputReference":
        return typing.cast("DmsEndpointKinesisSettingsOutputReference", jsii.get(self, "kinesisSettings"))

    @builtins.property
    @jsii.member(jsii_name="mongodbSettings")
    def mongodb_settings(self) -> "DmsEndpointMongodbSettingsOutputReference":
        return typing.cast("DmsEndpointMongodbSettingsOutputReference", jsii.get(self, "mongodbSettings"))

    @builtins.property
    @jsii.member(jsii_name="redshiftSettings")
    def redshift_settings(self) -> "DmsEndpointRedshiftSettingsOutputReference":
        return typing.cast("DmsEndpointRedshiftSettingsOutputReference", jsii.get(self, "redshiftSettings"))

    @builtins.property
    @jsii.member(jsii_name="s3Settings")
    def s3_settings(self) -> "DmsEndpointS3SettingsOutputReference":
        return typing.cast("DmsEndpointS3SettingsOutputReference", jsii.get(self, "s3Settings"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DmsEndpointTimeoutsOutputReference":
        return typing.cast("DmsEndpointTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="certificateArnInput")
    def certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchSettingsInput")
    def elasticsearch_settings_input(
        self,
    ) -> typing.Optional["DmsEndpointElasticsearchSettings"]:
        return typing.cast(typing.Optional["DmsEndpointElasticsearchSettings"], jsii.get(self, "elasticsearchSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointIdInput")
    def endpoint_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointIdInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointTypeInput")
    def endpoint_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="engineNameInput")
    def engine_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineNameInput"))

    @builtins.property
    @jsii.member(jsii_name="extraConnectionAttributesInput")
    def extra_connection_attributes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extraConnectionAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kafkaSettingsInput")
    def kafka_settings_input(self) -> typing.Optional["DmsEndpointKafkaSettings"]:
        return typing.cast(typing.Optional["DmsEndpointKafkaSettings"], jsii.get(self, "kafkaSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisSettingsInput")
    def kinesis_settings_input(self) -> typing.Optional["DmsEndpointKinesisSettings"]:
        return typing.cast(typing.Optional["DmsEndpointKinesisSettings"], jsii.get(self, "kinesisSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="mongodbSettingsInput")
    def mongodb_settings_input(self) -> typing.Optional["DmsEndpointMongodbSettings"]:
        return typing.cast(typing.Optional["DmsEndpointMongodbSettings"], jsii.get(self, "mongodbSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftSettingsInput")
    def redshift_settings_input(self) -> typing.Optional["DmsEndpointRedshiftSettings"]:
        return typing.cast(typing.Optional["DmsEndpointRedshiftSettings"], jsii.get(self, "redshiftSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3SettingsInput")
    def s3_settings_input(self) -> typing.Optional["DmsEndpointS3Settings"]:
        return typing.cast(typing.Optional["DmsEndpointS3Settings"], jsii.get(self, "s3SettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="secretsManagerAccessRoleArnInput")
    def secrets_manager_access_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretsManagerAccessRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="secretsManagerArnInput")
    def secrets_manager_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretsManagerArnInput"))

    @builtins.property
    @jsii.member(jsii_name="serverNameInput")
    def server_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleInput")
    def service_access_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccessRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="sslModeInput")
    def ssl_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslModeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DmsEndpointTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DmsEndpointTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @certificate_arn.setter
    def certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "certificate_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "database_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="endpointId")
    def endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointId"))

    @endpoint_id.setter
    def endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "endpoint_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointId", value)

    @builtins.property
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointType"))

    @endpoint_type.setter
    def endpoint_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "endpoint_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointType", value)

    @builtins.property
    @jsii.member(jsii_name="engineName")
    def engine_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineName"))

    @engine_name.setter
    def engine_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "engine_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineName", value)

    @builtins.property
    @jsii.member(jsii_name="extraConnectionAttributes")
    def extra_connection_attributes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "extraConnectionAttributes"))

    @extra_connection_attributes.setter
    def extra_connection_attributes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "extra_connection_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extraConnectionAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "kms_key_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="secretsManagerAccessRoleArn")
    def secrets_manager_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretsManagerAccessRoleArn"))

    @secrets_manager_access_role_arn.setter
    def secrets_manager_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "secrets_manager_access_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretsManagerAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="secretsManagerArn")
    def secrets_manager_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretsManagerArn"))

    @secrets_manager_arn.setter
    def secrets_manager_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "secrets_manager_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretsManagerArn", value)

    @builtins.property
    @jsii.member(jsii_name="serverName")
    def server_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverName"))

    @server_name.setter
    def server_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "server_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRole")
    def service_access_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessRole"))

    @service_access_role.setter
    def service_access_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "service_access_role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessRole", value)

    @builtins.property
    @jsii.member(jsii_name="sslMode")
    def ssl_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslMode"))

    @ssl_mode.setter
    def ssl_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "ssl_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslMode", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpoint, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dms.DmsEndpointConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "endpoint_id": "endpointId",
        "endpoint_type": "endpointType",
        "engine_name": "engineName",
        "certificate_arn": "certificateArn",
        "database_name": "databaseName",
        "elasticsearch_settings": "elasticsearchSettings",
        "extra_connection_attributes": "extraConnectionAttributes",
        "id": "id",
        "kafka_settings": "kafkaSettings",
        "kinesis_settings": "kinesisSettings",
        "kms_key_arn": "kmsKeyArn",
        "mongodb_settings": "mongodbSettings",
        "password": "password",
        "port": "port",
        "redshift_settings": "redshiftSettings",
        "s3_settings": "s3Settings",
        "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
        "secrets_manager_arn": "secretsManagerArn",
        "server_name": "serverName",
        "service_access_role": "serviceAccessRole",
        "ssl_mode": "sslMode",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "username": "username",
    },
)
class DmsEndpointConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        endpoint_id: builtins.str,
        endpoint_type: builtins.str,
        engine_name: builtins.str,
        certificate_arn: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        elasticsearch_settings: typing.Optional[typing.Union["DmsEndpointElasticsearchSettings", typing.Dict[str, typing.Any]]] = None,
        extra_connection_attributes: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kafka_settings: typing.Optional[typing.Union["DmsEndpointKafkaSettings", typing.Dict[str, typing.Any]]] = None,
        kinesis_settings: typing.Optional[typing.Union["DmsEndpointKinesisSettings", typing.Dict[str, typing.Any]]] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        mongodb_settings: typing.Optional[typing.Union["DmsEndpointMongodbSettings", typing.Dict[str, typing.Any]]] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        redshift_settings: typing.Optional[typing.Union["DmsEndpointRedshiftSettings", typing.Dict[str, typing.Any]]] = None,
        s3_settings: typing.Optional[typing.Union["DmsEndpointS3Settings", typing.Dict[str, typing.Any]]] = None,
        secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
        secrets_manager_arn: typing.Optional[builtins.str] = None,
        server_name: typing.Optional[builtins.str] = None,
        service_access_role: typing.Optional[builtins.str] = None,
        ssl_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DmsEndpointTimeouts", typing.Dict[str, typing.Any]]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Database Migration Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_id DmsEndpoint#endpoint_id}.
        :param endpoint_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_type DmsEndpoint#endpoint_type}.
        :param engine_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#engine_name DmsEndpoint#engine_name}.
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#certificate_arn DmsEndpoint#certificate_arn}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#database_name DmsEndpoint#database_name}.
        :param elasticsearch_settings: elasticsearch_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#elasticsearch_settings DmsEndpoint#elasticsearch_settings}
        :param extra_connection_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#extra_connection_attributes DmsEndpoint#extra_connection_attributes}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#id DmsEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kafka_settings: kafka_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kafka_settings DmsEndpoint#kafka_settings}
        :param kinesis_settings: kinesis_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kinesis_settings DmsEndpoint#kinesis_settings}
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kms_key_arn DmsEndpoint#kms_key_arn}.
        :param mongodb_settings: mongodb_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#mongodb_settings DmsEndpoint#mongodb_settings}
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#password DmsEndpoint#password}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#port DmsEndpoint#port}.
        :param redshift_settings: redshift_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#redshift_settings DmsEndpoint#redshift_settings}
        :param s3_settings: s3_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#s3_settings DmsEndpoint#s3_settings}
        :param secrets_manager_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#secrets_manager_access_role_arn DmsEndpoint#secrets_manager_access_role_arn}.
        :param secrets_manager_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#secrets_manager_arn DmsEndpoint#secrets_manager_arn}.
        :param server_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_name DmsEndpoint#server_name}.
        :param service_access_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role DmsEndpoint#service_access_role}.
        :param ssl_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_mode DmsEndpoint#ssl_mode}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#tags DmsEndpoint#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#tags_all DmsEndpoint#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#timeouts DmsEndpoint#timeouts}
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#username DmsEndpoint#username}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(elasticsearch_settings, dict):
            elasticsearch_settings = DmsEndpointElasticsearchSettings(**elasticsearch_settings)
        if isinstance(kafka_settings, dict):
            kafka_settings = DmsEndpointKafkaSettings(**kafka_settings)
        if isinstance(kinesis_settings, dict):
            kinesis_settings = DmsEndpointKinesisSettings(**kinesis_settings)
        if isinstance(mongodb_settings, dict):
            mongodb_settings = DmsEndpointMongodbSettings(**mongodb_settings)
        if isinstance(redshift_settings, dict):
            redshift_settings = DmsEndpointRedshiftSettings(**redshift_settings)
        if isinstance(s3_settings, dict):
            s3_settings = DmsEndpointS3Settings(**s3_settings)
        if isinstance(timeouts, dict):
            timeouts = DmsEndpointTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DmsEndpointConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument endpoint_id", value=endpoint_id, expected_type=type_hints["endpoint_id"])
            check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
            check_type(argname="argument engine_name", value=engine_name, expected_type=type_hints["engine_name"])
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument elasticsearch_settings", value=elasticsearch_settings, expected_type=type_hints["elasticsearch_settings"])
            check_type(argname="argument extra_connection_attributes", value=extra_connection_attributes, expected_type=type_hints["extra_connection_attributes"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kafka_settings", value=kafka_settings, expected_type=type_hints["kafka_settings"])
            check_type(argname="argument kinesis_settings", value=kinesis_settings, expected_type=type_hints["kinesis_settings"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument mongodb_settings", value=mongodb_settings, expected_type=type_hints["mongodb_settings"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument redshift_settings", value=redshift_settings, expected_type=type_hints["redshift_settings"])
            check_type(argname="argument s3_settings", value=s3_settings, expected_type=type_hints["s3_settings"])
            check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
            check_type(argname="argument secrets_manager_arn", value=secrets_manager_arn, expected_type=type_hints["secrets_manager_arn"])
            check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
            check_type(argname="argument service_access_role", value=service_access_role, expected_type=type_hints["service_access_role"])
            check_type(argname="argument ssl_mode", value=ssl_mode, expected_type=type_hints["ssl_mode"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_id": endpoint_id,
            "endpoint_type": endpoint_type,
            "engine_name": engine_name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if certificate_arn is not None:
            self._values["certificate_arn"] = certificate_arn
        if database_name is not None:
            self._values["database_name"] = database_name
        if elasticsearch_settings is not None:
            self._values["elasticsearch_settings"] = elasticsearch_settings
        if extra_connection_attributes is not None:
            self._values["extra_connection_attributes"] = extra_connection_attributes
        if id is not None:
            self._values["id"] = id
        if kafka_settings is not None:
            self._values["kafka_settings"] = kafka_settings
        if kinesis_settings is not None:
            self._values["kinesis_settings"] = kinesis_settings
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if mongodb_settings is not None:
            self._values["mongodb_settings"] = mongodb_settings
        if password is not None:
            self._values["password"] = password
        if port is not None:
            self._values["port"] = port
        if redshift_settings is not None:
            self._values["redshift_settings"] = redshift_settings
        if s3_settings is not None:
            self._values["s3_settings"] = s3_settings
        if secrets_manager_access_role_arn is not None:
            self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
        if secrets_manager_arn is not None:
            self._values["secrets_manager_arn"] = secrets_manager_arn
        if server_name is not None:
            self._values["server_name"] = server_name
        if service_access_role is not None:
            self._values["service_access_role"] = service_access_role
        if ssl_mode is not None:
            self._values["ssl_mode"] = ssl_mode
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def endpoint_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_id DmsEndpoint#endpoint_id}.'''
        result = self._values.get("endpoint_id")
        assert result is not None, "Required property 'endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_type DmsEndpoint#endpoint_type}.'''
        result = self._values.get("endpoint_type")
        assert result is not None, "Required property 'endpoint_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#engine_name DmsEndpoint#engine_name}.'''
        result = self._values.get("engine_name")
        assert result is not None, "Required property 'engine_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#certificate_arn DmsEndpoint#certificate_arn}.'''
        result = self._values.get("certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#database_name DmsEndpoint#database_name}.'''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticsearch_settings(
        self,
    ) -> typing.Optional["DmsEndpointElasticsearchSettings"]:
        '''elasticsearch_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#elasticsearch_settings DmsEndpoint#elasticsearch_settings}
        '''
        result = self._values.get("elasticsearch_settings")
        return typing.cast(typing.Optional["DmsEndpointElasticsearchSettings"], result)

    @builtins.property
    def extra_connection_attributes(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#extra_connection_attributes DmsEndpoint#extra_connection_attributes}.'''
        result = self._values.get("extra_connection_attributes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#id DmsEndpoint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kafka_settings(self) -> typing.Optional["DmsEndpointKafkaSettings"]:
        '''kafka_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kafka_settings DmsEndpoint#kafka_settings}
        '''
        result = self._values.get("kafka_settings")
        return typing.cast(typing.Optional["DmsEndpointKafkaSettings"], result)

    @builtins.property
    def kinesis_settings(self) -> typing.Optional["DmsEndpointKinesisSettings"]:
        '''kinesis_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kinesis_settings DmsEndpoint#kinesis_settings}
        '''
        result = self._values.get("kinesis_settings")
        return typing.cast(typing.Optional["DmsEndpointKinesisSettings"], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kms_key_arn DmsEndpoint#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mongodb_settings(self) -> typing.Optional["DmsEndpointMongodbSettings"]:
        '''mongodb_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#mongodb_settings DmsEndpoint#mongodb_settings}
        '''
        result = self._values.get("mongodb_settings")
        return typing.cast(typing.Optional["DmsEndpointMongodbSettings"], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#password DmsEndpoint#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#port DmsEndpoint#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def redshift_settings(self) -> typing.Optional["DmsEndpointRedshiftSettings"]:
        '''redshift_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#redshift_settings DmsEndpoint#redshift_settings}
        '''
        result = self._values.get("redshift_settings")
        return typing.cast(typing.Optional["DmsEndpointRedshiftSettings"], result)

    @builtins.property
    def s3_settings(self) -> typing.Optional["DmsEndpointS3Settings"]:
        '''s3_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#s3_settings DmsEndpoint#s3_settings}
        '''
        result = self._values.get("s3_settings")
        return typing.cast(typing.Optional["DmsEndpointS3Settings"], result)

    @builtins.property
    def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#secrets_manager_access_role_arn DmsEndpoint#secrets_manager_access_role_arn}.'''
        result = self._values.get("secrets_manager_access_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secrets_manager_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#secrets_manager_arn DmsEndpoint#secrets_manager_arn}.'''
        result = self._values.get("secrets_manager_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_name DmsEndpoint#server_name}.'''
        result = self._values.get("server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_access_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role DmsEndpoint#service_access_role}.'''
        result = self._values.get("service_access_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_mode DmsEndpoint#ssl_mode}.'''
        result = self._values.get("ssl_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#tags DmsEndpoint#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#tags_all DmsEndpoint#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DmsEndpointTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#timeouts DmsEndpoint#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DmsEndpointTimeouts"], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#username DmsEndpoint#username}.'''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dms.DmsEndpointElasticsearchSettings",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_uri": "endpointUri",
        "service_access_role_arn": "serviceAccessRoleArn",
        "error_retry_duration": "errorRetryDuration",
        "full_load_error_percentage": "fullLoadErrorPercentage",
    },
)
class DmsEndpointElasticsearchSettings:
    def __init__(
        self,
        *,
        endpoint_uri: builtins.str,
        service_access_role_arn: builtins.str,
        error_retry_duration: typing.Optional[jsii.Number] = None,
        full_load_error_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param endpoint_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_uri DmsEndpoint#endpoint_uri}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.
        :param error_retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#error_retry_duration DmsEndpoint#error_retry_duration}.
        :param full_load_error_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#full_load_error_percentage DmsEndpoint#full_load_error_percentage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEndpointElasticsearchSettings.__init__)
            check_type(argname="argument endpoint_uri", value=endpoint_uri, expected_type=type_hints["endpoint_uri"])
            check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
            check_type(argname="argument error_retry_duration", value=error_retry_duration, expected_type=type_hints["error_retry_duration"])
            check_type(argname="argument full_load_error_percentage", value=full_load_error_percentage, expected_type=type_hints["full_load_error_percentage"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_uri": endpoint_uri,
            "service_access_role_arn": service_access_role_arn,
        }
        if error_retry_duration is not None:
            self._values["error_retry_duration"] = error_retry_duration
        if full_load_error_percentage is not None:
            self._values["full_load_error_percentage"] = full_load_error_percentage

    @builtins.property
    def endpoint_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_uri DmsEndpoint#endpoint_uri}.'''
        result = self._values.get("endpoint_uri")
        assert result is not None, "Required property 'endpoint_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_access_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.'''
        result = self._values.get("service_access_role_arn")
        assert result is not None, "Required property 'service_access_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_retry_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#error_retry_duration DmsEndpoint#error_retry_duration}.'''
        result = self._values.get("error_retry_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def full_load_error_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#full_load_error_percentage DmsEndpoint#full_load_error_percentage}.'''
        result = self._values.get("full_load_error_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointElasticsearchSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEndpointElasticsearchSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dms.DmsEndpointElasticsearchSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEndpointElasticsearchSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetErrorRetryDuration")
    def reset_error_retry_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorRetryDuration", []))

    @jsii.member(jsii_name="resetFullLoadErrorPercentage")
    def reset_full_load_error_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFullLoadErrorPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="endpointUriInput")
    def endpoint_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointUriInput"))

    @builtins.property
    @jsii.member(jsii_name="errorRetryDurationInput")
    def error_retry_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "errorRetryDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="fullLoadErrorPercentageInput")
    def full_load_error_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fullLoadErrorPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArnInput")
    def service_access_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccessRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointUri")
    def endpoint_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointUri"))

    @endpoint_uri.setter
    def endpoint_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointElasticsearchSettingsOutputReference, "endpoint_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointUri", value)

    @builtins.property
    @jsii.member(jsii_name="errorRetryDuration")
    def error_retry_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "errorRetryDuration"))

    @error_retry_duration.setter
    def error_retry_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointElasticsearchSettingsOutputReference, "error_retry_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorRetryDuration", value)

    @builtins.property
    @jsii.member(jsii_name="fullLoadErrorPercentage")
    def full_load_error_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fullLoadErrorPercentage"))

    @full_load_error_percentage.setter
    def full_load_error_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointElasticsearchSettingsOutputReference, "full_load_error_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fullLoadErrorPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessRoleArn"))

    @service_access_role_arn.setter
    def service_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointElasticsearchSettingsOutputReference, "service_access_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DmsEndpointElasticsearchSettings]:
        return typing.cast(typing.Optional[DmsEndpointElasticsearchSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DmsEndpointElasticsearchSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointElasticsearchSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dms.DmsEndpointKafkaSettings",
    jsii_struct_bases=[],
    name_mapping={
        "broker": "broker",
        "include_control_details": "includeControlDetails",
        "include_null_and_empty": "includeNullAndEmpty",
        "include_partition_value": "includePartitionValue",
        "include_table_alter_operations": "includeTableAlterOperations",
        "include_transaction_details": "includeTransactionDetails",
        "message_format": "messageFormat",
        "message_max_bytes": "messageMaxBytes",
        "no_hex_prefix": "noHexPrefix",
        "partition_include_schema_table": "partitionIncludeSchemaTable",
        "sasl_password": "saslPassword",
        "sasl_username": "saslUsername",
        "security_protocol": "securityProtocol",
        "ssl_ca_certificate_arn": "sslCaCertificateArn",
        "ssl_client_certificate_arn": "sslClientCertificateArn",
        "ssl_client_key_arn": "sslClientKeyArn",
        "ssl_client_key_password": "sslClientKeyPassword",
        "topic": "topic",
    },
)
class DmsEndpointKafkaSettings:
    def __init__(
        self,
        *,
        broker: builtins.str,
        include_control_details: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_null_and_empty: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_partition_value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_transaction_details: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        message_format: typing.Optional[builtins.str] = None,
        message_max_bytes: typing.Optional[jsii.Number] = None,
        no_hex_prefix: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sasl_password: typing.Optional[builtins.str] = None,
        sasl_username: typing.Optional[builtins.str] = None,
        security_protocol: typing.Optional[builtins.str] = None,
        ssl_ca_certificate_arn: typing.Optional[builtins.str] = None,
        ssl_client_certificate_arn: typing.Optional[builtins.str] = None,
        ssl_client_key_arn: typing.Optional[builtins.str] = None,
        ssl_client_key_password: typing.Optional[builtins.str] = None,
        topic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param broker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#broker DmsEndpoint#broker}.
        :param include_control_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_control_details DmsEndpoint#include_control_details}.
        :param include_null_and_empty: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_null_and_empty DmsEndpoint#include_null_and_empty}.
        :param include_partition_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_partition_value DmsEndpoint#include_partition_value}.
        :param include_table_alter_operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_table_alter_operations DmsEndpoint#include_table_alter_operations}.
        :param include_transaction_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_transaction_details DmsEndpoint#include_transaction_details}.
        :param message_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_format DmsEndpoint#message_format}.
        :param message_max_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_max_bytes DmsEndpoint#message_max_bytes}.
        :param no_hex_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#no_hex_prefix DmsEndpoint#no_hex_prefix}.
        :param partition_include_schema_table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#partition_include_schema_table DmsEndpoint#partition_include_schema_table}.
        :param sasl_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#sasl_password DmsEndpoint#sasl_password}.
        :param sasl_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#sasl_username DmsEndpoint#sasl_username}.
        :param security_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#security_protocol DmsEndpoint#security_protocol}.
        :param ssl_ca_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_ca_certificate_arn DmsEndpoint#ssl_ca_certificate_arn}.
        :param ssl_client_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_certificate_arn DmsEndpoint#ssl_client_certificate_arn}.
        :param ssl_client_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_key_arn DmsEndpoint#ssl_client_key_arn}.
        :param ssl_client_key_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_key_password DmsEndpoint#ssl_client_key_password}.
        :param topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#topic DmsEndpoint#topic}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEndpointKafkaSettings.__init__)
            check_type(argname="argument broker", value=broker, expected_type=type_hints["broker"])
            check_type(argname="argument include_control_details", value=include_control_details, expected_type=type_hints["include_control_details"])
            check_type(argname="argument include_null_and_empty", value=include_null_and_empty, expected_type=type_hints["include_null_and_empty"])
            check_type(argname="argument include_partition_value", value=include_partition_value, expected_type=type_hints["include_partition_value"])
            check_type(argname="argument include_table_alter_operations", value=include_table_alter_operations, expected_type=type_hints["include_table_alter_operations"])
            check_type(argname="argument include_transaction_details", value=include_transaction_details, expected_type=type_hints["include_transaction_details"])
            check_type(argname="argument message_format", value=message_format, expected_type=type_hints["message_format"])
            check_type(argname="argument message_max_bytes", value=message_max_bytes, expected_type=type_hints["message_max_bytes"])
            check_type(argname="argument no_hex_prefix", value=no_hex_prefix, expected_type=type_hints["no_hex_prefix"])
            check_type(argname="argument partition_include_schema_table", value=partition_include_schema_table, expected_type=type_hints["partition_include_schema_table"])
            check_type(argname="argument sasl_password", value=sasl_password, expected_type=type_hints["sasl_password"])
            check_type(argname="argument sasl_username", value=sasl_username, expected_type=type_hints["sasl_username"])
            check_type(argname="argument security_protocol", value=security_protocol, expected_type=type_hints["security_protocol"])
            check_type(argname="argument ssl_ca_certificate_arn", value=ssl_ca_certificate_arn, expected_type=type_hints["ssl_ca_certificate_arn"])
            check_type(argname="argument ssl_client_certificate_arn", value=ssl_client_certificate_arn, expected_type=type_hints["ssl_client_certificate_arn"])
            check_type(argname="argument ssl_client_key_arn", value=ssl_client_key_arn, expected_type=type_hints["ssl_client_key_arn"])
            check_type(argname="argument ssl_client_key_password", value=ssl_client_key_password, expected_type=type_hints["ssl_client_key_password"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        self._values: typing.Dict[str, typing.Any] = {
            "broker": broker,
        }
        if include_control_details is not None:
            self._values["include_control_details"] = include_control_details
        if include_null_and_empty is not None:
            self._values["include_null_and_empty"] = include_null_and_empty
        if include_partition_value is not None:
            self._values["include_partition_value"] = include_partition_value
        if include_table_alter_operations is not None:
            self._values["include_table_alter_operations"] = include_table_alter_operations
        if include_transaction_details is not None:
            self._values["include_transaction_details"] = include_transaction_details
        if message_format is not None:
            self._values["message_format"] = message_format
        if message_max_bytes is not None:
            self._values["message_max_bytes"] = message_max_bytes
        if no_hex_prefix is not None:
            self._values["no_hex_prefix"] = no_hex_prefix
        if partition_include_schema_table is not None:
            self._values["partition_include_schema_table"] = partition_include_schema_table
        if sasl_password is not None:
            self._values["sasl_password"] = sasl_password
        if sasl_username is not None:
            self._values["sasl_username"] = sasl_username
        if security_protocol is not None:
            self._values["security_protocol"] = security_protocol
        if ssl_ca_certificate_arn is not None:
            self._values["ssl_ca_certificate_arn"] = ssl_ca_certificate_arn
        if ssl_client_certificate_arn is not None:
            self._values["ssl_client_certificate_arn"] = ssl_client_certificate_arn
        if ssl_client_key_arn is not None:
            self._values["ssl_client_key_arn"] = ssl_client_key_arn
        if ssl_client_key_password is not None:
            self._values["ssl_client_key_password"] = ssl_client_key_password
        if topic is not None:
            self._values["topic"] = topic

    @builtins.property
    def broker(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#broker DmsEndpoint#broker}.'''
        result = self._values.get("broker")
        assert result is not None, "Required property 'broker' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def include_control_details(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_control_details DmsEndpoint#include_control_details}.'''
        result = self._values.get("include_control_details")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_null_and_empty(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_null_and_empty DmsEndpoint#include_null_and_empty}.'''
        result = self._values.get("include_null_and_empty")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_partition_value(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_partition_value DmsEndpoint#include_partition_value}.'''
        result = self._values.get("include_partition_value")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_table_alter_operations(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_table_alter_operations DmsEndpoint#include_table_alter_operations}.'''
        result = self._values.get("include_table_alter_operations")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_transaction_details(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_transaction_details DmsEndpoint#include_transaction_details}.'''
        result = self._values.get("include_transaction_details")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def message_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_format DmsEndpoint#message_format}.'''
        result = self._values.get("message_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message_max_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_max_bytes DmsEndpoint#message_max_bytes}.'''
        result = self._values.get("message_max_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def no_hex_prefix(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#no_hex_prefix DmsEndpoint#no_hex_prefix}.'''
        result = self._values.get("no_hex_prefix")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def partition_include_schema_table(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#partition_include_schema_table DmsEndpoint#partition_include_schema_table}.'''
        result = self._values.get("partition_include_schema_table")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def sasl_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#sasl_password DmsEndpoint#sasl_password}.'''
        result = self._values.get("sasl_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sasl_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#sasl_username DmsEndpoint#sasl_username}.'''
        result = self._values.get("sasl_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#security_protocol DmsEndpoint#security_protocol}.'''
        result = self._values.get("security_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_ca_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_ca_certificate_arn DmsEndpoint#ssl_ca_certificate_arn}.'''
        result = self._values.get("ssl_ca_certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_client_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_certificate_arn DmsEndpoint#ssl_client_certificate_arn}.'''
        result = self._values.get("ssl_client_certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_client_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_key_arn DmsEndpoint#ssl_client_key_arn}.'''
        result = self._values.get("ssl_client_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_client_key_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_key_password DmsEndpoint#ssl_client_key_password}.'''
        result = self._values.get("ssl_client_key_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#topic DmsEndpoint#topic}.'''
        result = self._values.get("topic")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointKafkaSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEndpointKafkaSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dms.DmsEndpointKafkaSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEndpointKafkaSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIncludeControlDetails")
    def reset_include_control_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeControlDetails", []))

    @jsii.member(jsii_name="resetIncludeNullAndEmpty")
    def reset_include_null_and_empty(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeNullAndEmpty", []))

    @jsii.member(jsii_name="resetIncludePartitionValue")
    def reset_include_partition_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludePartitionValue", []))

    @jsii.member(jsii_name="resetIncludeTableAlterOperations")
    def reset_include_table_alter_operations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeTableAlterOperations", []))

    @jsii.member(jsii_name="resetIncludeTransactionDetails")
    def reset_include_transaction_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeTransactionDetails", []))

    @jsii.member(jsii_name="resetMessageFormat")
    def reset_message_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageFormat", []))

    @jsii.member(jsii_name="resetMessageMaxBytes")
    def reset_message_max_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageMaxBytes", []))

    @jsii.member(jsii_name="resetNoHexPrefix")
    def reset_no_hex_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoHexPrefix", []))

    @jsii.member(jsii_name="resetPartitionIncludeSchemaTable")
    def reset_partition_include_schema_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionIncludeSchemaTable", []))

    @jsii.member(jsii_name="resetSaslPassword")
    def reset_sasl_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaslPassword", []))

    @jsii.member(jsii_name="resetSaslUsername")
    def reset_sasl_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaslUsername", []))

    @jsii.member(jsii_name="resetSecurityProtocol")
    def reset_security_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityProtocol", []))

    @jsii.member(jsii_name="resetSslCaCertificateArn")
    def reset_ssl_ca_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslCaCertificateArn", []))

    @jsii.member(jsii_name="resetSslClientCertificateArn")
    def reset_ssl_client_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslClientCertificateArn", []))

    @jsii.member(jsii_name="resetSslClientKeyArn")
    def reset_ssl_client_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslClientKeyArn", []))

    @jsii.member(jsii_name="resetSslClientKeyPassword")
    def reset_ssl_client_key_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslClientKeyPassword", []))

    @jsii.member(jsii_name="resetTopic")
    def reset_topic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTopic", []))

    @builtins.property
    @jsii.member(jsii_name="brokerInput")
    def broker_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "brokerInput"))

    @builtins.property
    @jsii.member(jsii_name="includeControlDetailsInput")
    def include_control_details_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeControlDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeNullAndEmptyInput")
    def include_null_and_empty_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeNullAndEmptyInput"))

    @builtins.property
    @jsii.member(jsii_name="includePartitionValueInput")
    def include_partition_value_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includePartitionValueInput"))

    @builtins.property
    @jsii.member(jsii_name="includeTableAlterOperationsInput")
    def include_table_alter_operations_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeTableAlterOperationsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeTransactionDetailsInput")
    def include_transaction_details_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeTransactionDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageFormatInput")
    def message_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="messageMaxBytesInput")
    def message_max_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "messageMaxBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="noHexPrefixInput")
    def no_hex_prefix_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "noHexPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionIncludeSchemaTableInput")
    def partition_include_schema_table_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "partitionIncludeSchemaTableInput"))

    @builtins.property
    @jsii.member(jsii_name="saslPasswordInput")
    def sasl_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saslPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="saslUsernameInput")
    def sasl_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saslUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="securityProtocolInput")
    def security_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="sslCaCertificateArnInput")
    def ssl_ca_certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslCaCertificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sslClientCertificateArnInput")
    def ssl_client_certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslClientCertificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sslClientKeyArnInput")
    def ssl_client_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslClientKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sslClientKeyPasswordInput")
    def ssl_client_key_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslClientKeyPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="topicInput")
    def topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicInput"))

    @builtins.property
    @jsii.member(jsii_name="broker")
    def broker(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "broker"))

    @broker.setter
    def broker(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "broker").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "broker", value)

    @builtins.property
    @jsii.member(jsii_name="includeControlDetails")
    def include_control_details(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeControlDetails"))

    @include_control_details.setter
    def include_control_details(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "include_control_details").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeControlDetails", value)

    @builtins.property
    @jsii.member(jsii_name="includeNullAndEmpty")
    def include_null_and_empty(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeNullAndEmpty"))

    @include_null_and_empty.setter
    def include_null_and_empty(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "include_null_and_empty").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeNullAndEmpty", value)

    @builtins.property
    @jsii.member(jsii_name="includePartitionValue")
    def include_partition_value(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includePartitionValue"))

    @include_partition_value.setter
    def include_partition_value(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "include_partition_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includePartitionValue", value)

    @builtins.property
    @jsii.member(jsii_name="includeTableAlterOperations")
    def include_table_alter_operations(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeTableAlterOperations"))

    @include_table_alter_operations.setter
    def include_table_alter_operations(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "include_table_alter_operations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeTableAlterOperations", value)

    @builtins.property
    @jsii.member(jsii_name="includeTransactionDetails")
    def include_transaction_details(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeTransactionDetails"))

    @include_transaction_details.setter
    def include_transaction_details(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "include_transaction_details").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeTransactionDetails", value)

    @builtins.property
    @jsii.member(jsii_name="messageFormat")
    def message_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageFormat"))

    @message_format.setter
    def message_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "message_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageFormat", value)

    @builtins.property
    @jsii.member(jsii_name="messageMaxBytes")
    def message_max_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "messageMaxBytes"))

    @message_max_bytes.setter
    def message_max_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "message_max_bytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageMaxBytes", value)

    @builtins.property
    @jsii.member(jsii_name="noHexPrefix")
    def no_hex_prefix(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "noHexPrefix"))

    @no_hex_prefix.setter
    def no_hex_prefix(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "no_hex_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noHexPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="partitionIncludeSchemaTable")
    def partition_include_schema_table(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "partitionIncludeSchemaTable"))

    @partition_include_schema_table.setter
    def partition_include_schema_table(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "partition_include_schema_table").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionIncludeSchemaTable", value)

    @builtins.property
    @jsii.member(jsii_name="saslPassword")
    def sasl_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saslPassword"))

    @sasl_password.setter
    def sasl_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "sasl_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saslPassword", value)

    @builtins.property
    @jsii.member(jsii_name="saslUsername")
    def sasl_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saslUsername"))

    @sasl_username.setter
    def sasl_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "sasl_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saslUsername", value)

    @builtins.property
    @jsii.member(jsii_name="securityProtocol")
    def security_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityProtocol"))

    @security_protocol.setter
    def security_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "security_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="sslCaCertificateArn")
    def ssl_ca_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslCaCertificateArn"))

    @ssl_ca_certificate_arn.setter
    def ssl_ca_certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "ssl_ca_certificate_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslCaCertificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="sslClientCertificateArn")
    def ssl_client_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslClientCertificateArn"))

    @ssl_client_certificate_arn.setter
    def ssl_client_certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "ssl_client_certificate_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslClientCertificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="sslClientKeyArn")
    def ssl_client_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslClientKeyArn"))

    @ssl_client_key_arn.setter
    def ssl_client_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "ssl_client_key_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslClientKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="sslClientKeyPassword")
    def ssl_client_key_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslClientKeyPassword"))

    @ssl_client_key_password.setter
    def ssl_client_key_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "ssl_client_key_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslClientKeyPassword", value)

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @topic.setter
    def topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "topic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topic", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DmsEndpointKafkaSettings]:
        return typing.cast(typing.Optional[DmsEndpointKafkaSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DmsEndpointKafkaSettings]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKafkaSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dms.DmsEndpointKinesisSettings",
    jsii_struct_bases=[],
    name_mapping={
        "include_control_details": "includeControlDetails",
        "include_null_and_empty": "includeNullAndEmpty",
        "include_partition_value": "includePartitionValue",
        "include_table_alter_operations": "includeTableAlterOperations",
        "include_transaction_details": "includeTransactionDetails",
        "message_format": "messageFormat",
        "partition_include_schema_table": "partitionIncludeSchemaTable",
        "service_access_role_arn": "serviceAccessRoleArn",
        "stream_arn": "streamArn",
    },
)
class DmsEndpointKinesisSettings:
    def __init__(
        self,
        *,
        include_control_details: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_null_and_empty: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_partition_value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_transaction_details: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        message_format: typing.Optional[builtins.str] = None,
        partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_access_role_arn: typing.Optional[builtins.str] = None,
        stream_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param include_control_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_control_details DmsEndpoint#include_control_details}.
        :param include_null_and_empty: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_null_and_empty DmsEndpoint#include_null_and_empty}.
        :param include_partition_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_partition_value DmsEndpoint#include_partition_value}.
        :param include_table_alter_operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_table_alter_operations DmsEndpoint#include_table_alter_operations}.
        :param include_transaction_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_transaction_details DmsEndpoint#include_transaction_details}.
        :param message_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_format DmsEndpoint#message_format}.
        :param partition_include_schema_table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#partition_include_schema_table DmsEndpoint#partition_include_schema_table}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.
        :param stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#stream_arn DmsEndpoint#stream_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEndpointKinesisSettings.__init__)
            check_type(argname="argument include_control_details", value=include_control_details, expected_type=type_hints["include_control_details"])
            check_type(argname="argument include_null_and_empty", value=include_null_and_empty, expected_type=type_hints["include_null_and_empty"])
            check_type(argname="argument include_partition_value", value=include_partition_value, expected_type=type_hints["include_partition_value"])
            check_type(argname="argument include_table_alter_operations", value=include_table_alter_operations, expected_type=type_hints["include_table_alter_operations"])
            check_type(argname="argument include_transaction_details", value=include_transaction_details, expected_type=type_hints["include_transaction_details"])
            check_type(argname="argument message_format", value=message_format, expected_type=type_hints["message_format"])
            check_type(argname="argument partition_include_schema_table", value=partition_include_schema_table, expected_type=type_hints["partition_include_schema_table"])
            check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
            check_type(argname="argument stream_arn", value=stream_arn, expected_type=type_hints["stream_arn"])
        self._values: typing.Dict[str, typing.Any] = {}
        if include_control_details is not None:
            self._values["include_control_details"] = include_control_details
        if include_null_and_empty is not None:
            self._values["include_null_and_empty"] = include_null_and_empty
        if include_partition_value is not None:
            self._values["include_partition_value"] = include_partition_value
        if include_table_alter_operations is not None:
            self._values["include_table_alter_operations"] = include_table_alter_operations
        if include_transaction_details is not None:
            self._values["include_transaction_details"] = include_transaction_details
        if message_format is not None:
            self._values["message_format"] = message_format
        if partition_include_schema_table is not None:
            self._values["partition_include_schema_table"] = partition_include_schema_table
        if service_access_role_arn is not None:
            self._values["service_access_role_arn"] = service_access_role_arn
        if stream_arn is not None:
            self._values["stream_arn"] = stream_arn

    @builtins.property
    def include_control_details(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_control_details DmsEndpoint#include_control_details}.'''
        result = self._values.get("include_control_details")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_null_and_empty(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_null_and_empty DmsEndpoint#include_null_and_empty}.'''
        result = self._values.get("include_null_and_empty")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_partition_value(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_partition_value DmsEndpoint#include_partition_value}.'''
        result = self._values.get("include_partition_value")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_table_alter_operations(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_table_alter_operations DmsEndpoint#include_table_alter_operations}.'''
        result = self._values.get("include_table_alter_operations")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_transaction_details(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_transaction_details DmsEndpoint#include_transaction_details}.'''
        result = self._values.get("include_transaction_details")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def message_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_format DmsEndpoint#message_format}.'''
        result = self._values.get("message_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition_include_schema_table(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#partition_include_schema_table DmsEndpoint#partition_include_schema_table}.'''
        result = self._values.get("partition_include_schema_table")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def service_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.'''
        result = self._values.get("service_access_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stream_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#stream_arn DmsEndpoint#stream_arn}.'''
        result = self._values.get("stream_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointKinesisSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEndpointKinesisSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dms.DmsEndpointKinesisSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEndpointKinesisSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIncludeControlDetails")
    def reset_include_control_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeControlDetails", []))

    @jsii.member(jsii_name="resetIncludeNullAndEmpty")
    def reset_include_null_and_empty(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeNullAndEmpty", []))

    @jsii.member(jsii_name="resetIncludePartitionValue")
    def reset_include_partition_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludePartitionValue", []))

    @jsii.member(jsii_name="resetIncludeTableAlterOperations")
    def reset_include_table_alter_operations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeTableAlterOperations", []))

    @jsii.member(jsii_name="resetIncludeTransactionDetails")
    def reset_include_transaction_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeTransactionDetails", []))

    @jsii.member(jsii_name="resetMessageFormat")
    def reset_message_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageFormat", []))

    @jsii.member(jsii_name="resetPartitionIncludeSchemaTable")
    def reset_partition_include_schema_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionIncludeSchemaTable", []))

    @jsii.member(jsii_name="resetServiceAccessRoleArn")
    def reset_service_access_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccessRoleArn", []))

    @jsii.member(jsii_name="resetStreamArn")
    def reset_stream_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreamArn", []))

    @builtins.property
    @jsii.member(jsii_name="includeControlDetailsInput")
    def include_control_details_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeControlDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeNullAndEmptyInput")
    def include_null_and_empty_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeNullAndEmptyInput"))

    @builtins.property
    @jsii.member(jsii_name="includePartitionValueInput")
    def include_partition_value_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includePartitionValueInput"))

    @builtins.property
    @jsii.member(jsii_name="includeTableAlterOperationsInput")
    def include_table_alter_operations_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeTableAlterOperationsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeTransactionDetailsInput")
    def include_transaction_details_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeTransactionDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageFormatInput")
    def message_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionIncludeSchemaTableInput")
    def partition_include_schema_table_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "partitionIncludeSchemaTableInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArnInput")
    def service_access_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccessRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="streamArnInput")
    def stream_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamArnInput"))

    @builtins.property
    @jsii.member(jsii_name="includeControlDetails")
    def include_control_details(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeControlDetails"))

    @include_control_details.setter
    def include_control_details(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKinesisSettingsOutputReference, "include_control_details").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeControlDetails", value)

    @builtins.property
    @jsii.member(jsii_name="includeNullAndEmpty")
    def include_null_and_empty(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeNullAndEmpty"))

    @include_null_and_empty.setter
    def include_null_and_empty(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKinesisSettingsOutputReference, "include_null_and_empty").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeNullAndEmpty", value)

    @builtins.property
    @jsii.member(jsii_name="includePartitionValue")
    def include_partition_value(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includePartitionValue"))

    @include_partition_value.setter
    def include_partition_value(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKinesisSettingsOutputReference, "include_partition_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includePartitionValue", value)

    @builtins.property
    @jsii.member(jsii_name="includeTableAlterOperations")
    def include_table_alter_operations(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeTableAlterOperations"))

    @include_table_alter_operations.setter
    def include_table_alter_operations(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKinesisSettingsOutputReference, "include_table_alter_operations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeTableAlterOperations", value)

    @builtins.property
    @jsii.member(jsii_name="includeTransactionDetails")
    def include_transaction_details(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeTransactionDetails"))

    @include_transaction_details.setter
    def include_transaction_details(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKinesisSettingsOutputReference, "include_transaction_details").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeTransactionDetails", value)

    @builtins.property
    @jsii.member(jsii_name="messageFormat")
    def message_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageFormat"))

    @message_format.setter
    def message_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKinesisSettingsOutputReference, "message_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageFormat", value)

    @builtins.property
    @jsii.member(jsii_name="partitionIncludeSchemaTable")
    def partition_include_schema_table(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "partitionIncludeSchemaTable"))

    @partition_include_schema_table.setter
    def partition_include_schema_table(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKinesisSettingsOutputReference, "partition_include_schema_table").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionIncludeSchemaTable", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessRoleArn"))

    @service_access_role_arn.setter
    def service_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKinesisSettingsOutputReference, "service_access_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="streamArn")
    def stream_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamArn"))

    @stream_arn.setter
    def stream_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKinesisSettingsOutputReference, "stream_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DmsEndpointKinesisSettings]:
        return typing.cast(typing.Optional[DmsEndpointKinesisSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DmsEndpointKinesisSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointKinesisSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dms.DmsEndpointMongodbSettings",
    jsii_struct_bases=[],
    name_mapping={
        "auth_mechanism": "authMechanism",
        "auth_source": "authSource",
        "auth_type": "authType",
        "docs_to_investigate": "docsToInvestigate",
        "extract_doc_id": "extractDocId",
        "nesting_level": "nestingLevel",
    },
)
class DmsEndpointMongodbSettings:
    def __init__(
        self,
        *,
        auth_mechanism: typing.Optional[builtins.str] = None,
        auth_source: typing.Optional[builtins.str] = None,
        auth_type: typing.Optional[builtins.str] = None,
        docs_to_investigate: typing.Optional[builtins.str] = None,
        extract_doc_id: typing.Optional[builtins.str] = None,
        nesting_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_mechanism: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_mechanism DmsEndpoint#auth_mechanism}.
        :param auth_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_source DmsEndpoint#auth_source}.
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_type DmsEndpoint#auth_type}.
        :param docs_to_investigate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#docs_to_investigate DmsEndpoint#docs_to_investigate}.
        :param extract_doc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#extract_doc_id DmsEndpoint#extract_doc_id}.
        :param nesting_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#nesting_level DmsEndpoint#nesting_level}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEndpointMongodbSettings.__init__)
            check_type(argname="argument auth_mechanism", value=auth_mechanism, expected_type=type_hints["auth_mechanism"])
            check_type(argname="argument auth_source", value=auth_source, expected_type=type_hints["auth_source"])
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument docs_to_investigate", value=docs_to_investigate, expected_type=type_hints["docs_to_investigate"])
            check_type(argname="argument extract_doc_id", value=extract_doc_id, expected_type=type_hints["extract_doc_id"])
            check_type(argname="argument nesting_level", value=nesting_level, expected_type=type_hints["nesting_level"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auth_mechanism is not None:
            self._values["auth_mechanism"] = auth_mechanism
        if auth_source is not None:
            self._values["auth_source"] = auth_source
        if auth_type is not None:
            self._values["auth_type"] = auth_type
        if docs_to_investigate is not None:
            self._values["docs_to_investigate"] = docs_to_investigate
        if extract_doc_id is not None:
            self._values["extract_doc_id"] = extract_doc_id
        if nesting_level is not None:
            self._values["nesting_level"] = nesting_level

    @builtins.property
    def auth_mechanism(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_mechanism DmsEndpoint#auth_mechanism}.'''
        result = self._values.get("auth_mechanism")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_source(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_source DmsEndpoint#auth_source}.'''
        result = self._values.get("auth_source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_type DmsEndpoint#auth_type}.'''
        result = self._values.get("auth_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docs_to_investigate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#docs_to_investigate DmsEndpoint#docs_to_investigate}.'''
        result = self._values.get("docs_to_investigate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extract_doc_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#extract_doc_id DmsEndpoint#extract_doc_id}.'''
        result = self._values.get("extract_doc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nesting_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#nesting_level DmsEndpoint#nesting_level}.'''
        result = self._values.get("nesting_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointMongodbSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEndpointMongodbSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dms.DmsEndpointMongodbSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEndpointMongodbSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthMechanism")
    def reset_auth_mechanism(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthMechanism", []))

    @jsii.member(jsii_name="resetAuthSource")
    def reset_auth_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthSource", []))

    @jsii.member(jsii_name="resetAuthType")
    def reset_auth_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthType", []))

    @jsii.member(jsii_name="resetDocsToInvestigate")
    def reset_docs_to_investigate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocsToInvestigate", []))

    @jsii.member(jsii_name="resetExtractDocId")
    def reset_extract_doc_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtractDocId", []))

    @jsii.member(jsii_name="resetNestingLevel")
    def reset_nesting_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNestingLevel", []))

    @builtins.property
    @jsii.member(jsii_name="authMechanismInput")
    def auth_mechanism_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authMechanismInput"))

    @builtins.property
    @jsii.member(jsii_name="authSourceInput")
    def auth_source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="authTypeInput")
    def auth_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="docsToInvestigateInput")
    def docs_to_investigate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "docsToInvestigateInput"))

    @builtins.property
    @jsii.member(jsii_name="extractDocIdInput")
    def extract_doc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extractDocIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nestingLevelInput")
    def nesting_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nestingLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="authMechanism")
    def auth_mechanism(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authMechanism"))

    @auth_mechanism.setter
    def auth_mechanism(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointMongodbSettingsOutputReference, "auth_mechanism").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authMechanism", value)

    @builtins.property
    @jsii.member(jsii_name="authSource")
    def auth_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authSource"))

    @auth_source.setter
    def auth_source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointMongodbSettingsOutputReference, "auth_source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authSource", value)

    @builtins.property
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authType"))

    @auth_type.setter
    def auth_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointMongodbSettingsOutputReference, "auth_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authType", value)

    @builtins.property
    @jsii.member(jsii_name="docsToInvestigate")
    def docs_to_investigate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "docsToInvestigate"))

    @docs_to_investigate.setter
    def docs_to_investigate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointMongodbSettingsOutputReference, "docs_to_investigate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "docsToInvestigate", value)

    @builtins.property
    @jsii.member(jsii_name="extractDocId")
    def extract_doc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "extractDocId"))

    @extract_doc_id.setter
    def extract_doc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointMongodbSettingsOutputReference, "extract_doc_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extractDocId", value)

    @builtins.property
    @jsii.member(jsii_name="nestingLevel")
    def nesting_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nestingLevel"))

    @nesting_level.setter
    def nesting_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointMongodbSettingsOutputReference, "nesting_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nestingLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DmsEndpointMongodbSettings]:
        return typing.cast(typing.Optional[DmsEndpointMongodbSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DmsEndpointMongodbSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointMongodbSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dms.DmsEndpointRedshiftSettings",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_folder": "bucketFolder",
        "bucket_name": "bucketName",
        "encryption_mode": "encryptionMode",
        "server_side_encryption_kms_key_id": "serverSideEncryptionKmsKeyId",
        "service_access_role_arn": "serviceAccessRoleArn",
    },
)
class DmsEndpointRedshiftSettings:
    def __init__(
        self,
        *,
        bucket_folder: typing.Optional[builtins.str] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        encryption_mode: typing.Optional[builtins.str] = None,
        server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        service_access_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_folder DmsEndpoint#bucket_folder}.
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_name DmsEndpoint#bucket_name}.
        :param encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encryption_mode DmsEndpoint#encryption_mode}.
        :param server_side_encryption_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_side_encryption_kms_key_id DmsEndpoint#server_side_encryption_kms_key_id}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEndpointRedshiftSettings.__init__)
            check_type(argname="argument bucket_folder", value=bucket_folder, expected_type=type_hints["bucket_folder"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument encryption_mode", value=encryption_mode, expected_type=type_hints["encryption_mode"])
            check_type(argname="argument server_side_encryption_kms_key_id", value=server_side_encryption_kms_key_id, expected_type=type_hints["server_side_encryption_kms_key_id"])
            check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_folder is not None:
            self._values["bucket_folder"] = bucket_folder
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if encryption_mode is not None:
            self._values["encryption_mode"] = encryption_mode
        if server_side_encryption_kms_key_id is not None:
            self._values["server_side_encryption_kms_key_id"] = server_side_encryption_kms_key_id
        if service_access_role_arn is not None:
            self._values["service_access_role_arn"] = service_access_role_arn

    @builtins.property
    def bucket_folder(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_folder DmsEndpoint#bucket_folder}.'''
        result = self._values.get("bucket_folder")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_name DmsEndpoint#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encryption_mode DmsEndpoint#encryption_mode}.'''
        result = self._values.get("encryption_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_encryption_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_side_encryption_kms_key_id DmsEndpoint#server_side_encryption_kms_key_id}.'''
        result = self._values.get("server_side_encryption_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.'''
        result = self._values.get("service_access_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointRedshiftSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEndpointRedshiftSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dms.DmsEndpointRedshiftSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEndpointRedshiftSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketFolder")
    def reset_bucket_folder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketFolder", []))

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetEncryptionMode")
    def reset_encryption_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionMode", []))

    @jsii.member(jsii_name="resetServerSideEncryptionKmsKeyId")
    def reset_server_side_encryption_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerSideEncryptionKmsKeyId", []))

    @jsii.member(jsii_name="resetServiceAccessRoleArn")
    def reset_service_access_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccessRoleArn", []))

    @builtins.property
    @jsii.member(jsii_name="bucketFolderInput")
    def bucket_folder_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketFolderInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionModeInput")
    def encryption_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionKmsKeyIdInput")
    def server_side_encryption_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverSideEncryptionKmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArnInput")
    def service_access_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccessRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketFolder")
    def bucket_folder(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketFolder"))

    @bucket_folder.setter
    def bucket_folder(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointRedshiftSettingsOutputReference, "bucket_folder").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketFolder", value)

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointRedshiftSettingsOutputReference, "bucket_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionMode")
    def encryption_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionMode"))

    @encryption_mode.setter
    def encryption_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointRedshiftSettingsOutputReference, "encryption_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionMode", value)

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionKmsKeyId")
    def server_side_encryption_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverSideEncryptionKmsKeyId"))

    @server_side_encryption_kms_key_id.setter
    def server_side_encryption_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointRedshiftSettingsOutputReference, "server_side_encryption_kms_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideEncryptionKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessRoleArn"))

    @service_access_role_arn.setter
    def service_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointRedshiftSettingsOutputReference, "service_access_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DmsEndpointRedshiftSettings]:
        return typing.cast(typing.Optional[DmsEndpointRedshiftSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DmsEndpointRedshiftSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointRedshiftSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dms.DmsEndpointS3Settings",
    jsii_struct_bases=[],
    name_mapping={
        "add_column_name": "addColumnName",
        "bucket_folder": "bucketFolder",
        "bucket_name": "bucketName",
        "canned_acl_for_objects": "cannedAclForObjects",
        "cdc_inserts_and_updates": "cdcInsertsAndUpdates",
        "cdc_inserts_only": "cdcInsertsOnly",
        "cdc_max_batch_interval": "cdcMaxBatchInterval",
        "cdc_min_file_size": "cdcMinFileSize",
        "cdc_path": "cdcPath",
        "compression_type": "compressionType",
        "csv_delimiter": "csvDelimiter",
        "csv_no_sup_value": "csvNoSupValue",
        "csv_null_value": "csvNullValue",
        "csv_row_delimiter": "csvRowDelimiter",
        "data_format": "dataFormat",
        "data_page_size": "dataPageSize",
        "date_partition_delimiter": "datePartitionDelimiter",
        "date_partition_enabled": "datePartitionEnabled",
        "date_partition_sequence": "datePartitionSequence",
        "dict_page_size_limit": "dictPageSizeLimit",
        "enable_statistics": "enableStatistics",
        "encoding_type": "encodingType",
        "encryption_mode": "encryptionMode",
        "external_table_definition": "externalTableDefinition",
        "ignore_headers_row": "ignoreHeadersRow",
        "include_op_for_full_load": "includeOpForFullLoad",
        "max_file_size": "maxFileSize",
        "parquet_timestamp_in_millisecond": "parquetTimestampInMillisecond",
        "parquet_version": "parquetVersion",
        "preserve_transactions": "preserveTransactions",
        "rfc4180": "rfc4180",
        "row_group_length": "rowGroupLength",
        "server_side_encryption_kms_key_id": "serverSideEncryptionKmsKeyId",
        "service_access_role_arn": "serviceAccessRoleArn",
        "timestamp_column_name": "timestampColumnName",
        "use_csv_no_sup_value": "useCsvNoSupValue",
    },
)
class DmsEndpointS3Settings:
    def __init__(
        self,
        *,
        add_column_name: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        bucket_folder: typing.Optional[builtins.str] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        canned_acl_for_objects: typing.Optional[builtins.str] = None,
        cdc_inserts_and_updates: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cdc_inserts_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cdc_max_batch_interval: typing.Optional[jsii.Number] = None,
        cdc_min_file_size: typing.Optional[jsii.Number] = None,
        cdc_path: typing.Optional[builtins.str] = None,
        compression_type: typing.Optional[builtins.str] = None,
        csv_delimiter: typing.Optional[builtins.str] = None,
        csv_no_sup_value: typing.Optional[builtins.str] = None,
        csv_null_value: typing.Optional[builtins.str] = None,
        csv_row_delimiter: typing.Optional[builtins.str] = None,
        data_format: typing.Optional[builtins.str] = None,
        data_page_size: typing.Optional[jsii.Number] = None,
        date_partition_delimiter: typing.Optional[builtins.str] = None,
        date_partition_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        date_partition_sequence: typing.Optional[builtins.str] = None,
        dict_page_size_limit: typing.Optional[jsii.Number] = None,
        enable_statistics: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encoding_type: typing.Optional[builtins.str] = None,
        encryption_mode: typing.Optional[builtins.str] = None,
        external_table_definition: typing.Optional[builtins.str] = None,
        ignore_headers_row: typing.Optional[jsii.Number] = None,
        include_op_for_full_load: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_file_size: typing.Optional[jsii.Number] = None,
        parquet_timestamp_in_millisecond: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        parquet_version: typing.Optional[builtins.str] = None,
        preserve_transactions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rfc4180: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        row_group_length: typing.Optional[jsii.Number] = None,
        server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        service_access_role_arn: typing.Optional[builtins.str] = None,
        timestamp_column_name: typing.Optional[builtins.str] = None,
        use_csv_no_sup_value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param add_column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#add_column_name DmsEndpoint#add_column_name}.
        :param bucket_folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_folder DmsEndpoint#bucket_folder}.
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_name DmsEndpoint#bucket_name}.
        :param canned_acl_for_objects: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#canned_acl_for_objects DmsEndpoint#canned_acl_for_objects}.
        :param cdc_inserts_and_updates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_inserts_and_updates DmsEndpoint#cdc_inserts_and_updates}.
        :param cdc_inserts_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_inserts_only DmsEndpoint#cdc_inserts_only}.
        :param cdc_max_batch_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_max_batch_interval DmsEndpoint#cdc_max_batch_interval}.
        :param cdc_min_file_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_min_file_size DmsEndpoint#cdc_min_file_size}.
        :param cdc_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_path DmsEndpoint#cdc_path}.
        :param compression_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#compression_type DmsEndpoint#compression_type}.
        :param csv_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_delimiter DmsEndpoint#csv_delimiter}.
        :param csv_no_sup_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_no_sup_value DmsEndpoint#csv_no_sup_value}.
        :param csv_null_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_null_value DmsEndpoint#csv_null_value}.
        :param csv_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_row_delimiter DmsEndpoint#csv_row_delimiter}.
        :param data_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#data_format DmsEndpoint#data_format}.
        :param data_page_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#data_page_size DmsEndpoint#data_page_size}.
        :param date_partition_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_delimiter DmsEndpoint#date_partition_delimiter}.
        :param date_partition_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_enabled DmsEndpoint#date_partition_enabled}.
        :param date_partition_sequence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_sequence DmsEndpoint#date_partition_sequence}.
        :param dict_page_size_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#dict_page_size_limit DmsEndpoint#dict_page_size_limit}.
        :param enable_statistics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#enable_statistics DmsEndpoint#enable_statistics}.
        :param encoding_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encoding_type DmsEndpoint#encoding_type}.
        :param encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encryption_mode DmsEndpoint#encryption_mode}.
        :param external_table_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#external_table_definition DmsEndpoint#external_table_definition}.
        :param ignore_headers_row: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ignore_headers_row DmsEndpoint#ignore_headers_row}.
        :param include_op_for_full_load: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_op_for_full_load DmsEndpoint#include_op_for_full_load}.
        :param max_file_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#max_file_size DmsEndpoint#max_file_size}.
        :param parquet_timestamp_in_millisecond: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#parquet_timestamp_in_millisecond DmsEndpoint#parquet_timestamp_in_millisecond}.
        :param parquet_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#parquet_version DmsEndpoint#parquet_version}.
        :param preserve_transactions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#preserve_transactions DmsEndpoint#preserve_transactions}.
        :param rfc4180: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#rfc_4180 DmsEndpoint#rfc_4180}.
        :param row_group_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#row_group_length DmsEndpoint#row_group_length}.
        :param server_side_encryption_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_side_encryption_kms_key_id DmsEndpoint#server_side_encryption_kms_key_id}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.
        :param timestamp_column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#timestamp_column_name DmsEndpoint#timestamp_column_name}.
        :param use_csv_no_sup_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#use_csv_no_sup_value DmsEndpoint#use_csv_no_sup_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEndpointS3Settings.__init__)
            check_type(argname="argument add_column_name", value=add_column_name, expected_type=type_hints["add_column_name"])
            check_type(argname="argument bucket_folder", value=bucket_folder, expected_type=type_hints["bucket_folder"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument canned_acl_for_objects", value=canned_acl_for_objects, expected_type=type_hints["canned_acl_for_objects"])
            check_type(argname="argument cdc_inserts_and_updates", value=cdc_inserts_and_updates, expected_type=type_hints["cdc_inserts_and_updates"])
            check_type(argname="argument cdc_inserts_only", value=cdc_inserts_only, expected_type=type_hints["cdc_inserts_only"])
            check_type(argname="argument cdc_max_batch_interval", value=cdc_max_batch_interval, expected_type=type_hints["cdc_max_batch_interval"])
            check_type(argname="argument cdc_min_file_size", value=cdc_min_file_size, expected_type=type_hints["cdc_min_file_size"])
            check_type(argname="argument cdc_path", value=cdc_path, expected_type=type_hints["cdc_path"])
            check_type(argname="argument compression_type", value=compression_type, expected_type=type_hints["compression_type"])
            check_type(argname="argument csv_delimiter", value=csv_delimiter, expected_type=type_hints["csv_delimiter"])
            check_type(argname="argument csv_no_sup_value", value=csv_no_sup_value, expected_type=type_hints["csv_no_sup_value"])
            check_type(argname="argument csv_null_value", value=csv_null_value, expected_type=type_hints["csv_null_value"])
            check_type(argname="argument csv_row_delimiter", value=csv_row_delimiter, expected_type=type_hints["csv_row_delimiter"])
            check_type(argname="argument data_format", value=data_format, expected_type=type_hints["data_format"])
            check_type(argname="argument data_page_size", value=data_page_size, expected_type=type_hints["data_page_size"])
            check_type(argname="argument date_partition_delimiter", value=date_partition_delimiter, expected_type=type_hints["date_partition_delimiter"])
            check_type(argname="argument date_partition_enabled", value=date_partition_enabled, expected_type=type_hints["date_partition_enabled"])
            check_type(argname="argument date_partition_sequence", value=date_partition_sequence, expected_type=type_hints["date_partition_sequence"])
            check_type(argname="argument dict_page_size_limit", value=dict_page_size_limit, expected_type=type_hints["dict_page_size_limit"])
            check_type(argname="argument enable_statistics", value=enable_statistics, expected_type=type_hints["enable_statistics"])
            check_type(argname="argument encoding_type", value=encoding_type, expected_type=type_hints["encoding_type"])
            check_type(argname="argument encryption_mode", value=encryption_mode, expected_type=type_hints["encryption_mode"])
            check_type(argname="argument external_table_definition", value=external_table_definition, expected_type=type_hints["external_table_definition"])
            check_type(argname="argument ignore_headers_row", value=ignore_headers_row, expected_type=type_hints["ignore_headers_row"])
            check_type(argname="argument include_op_for_full_load", value=include_op_for_full_load, expected_type=type_hints["include_op_for_full_load"])
            check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
            check_type(argname="argument parquet_timestamp_in_millisecond", value=parquet_timestamp_in_millisecond, expected_type=type_hints["parquet_timestamp_in_millisecond"])
            check_type(argname="argument parquet_version", value=parquet_version, expected_type=type_hints["parquet_version"])
            check_type(argname="argument preserve_transactions", value=preserve_transactions, expected_type=type_hints["preserve_transactions"])
            check_type(argname="argument rfc4180", value=rfc4180, expected_type=type_hints["rfc4180"])
            check_type(argname="argument row_group_length", value=row_group_length, expected_type=type_hints["row_group_length"])
            check_type(argname="argument server_side_encryption_kms_key_id", value=server_side_encryption_kms_key_id, expected_type=type_hints["server_side_encryption_kms_key_id"])
            check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
            check_type(argname="argument timestamp_column_name", value=timestamp_column_name, expected_type=type_hints["timestamp_column_name"])
            check_type(argname="argument use_csv_no_sup_value", value=use_csv_no_sup_value, expected_type=type_hints["use_csv_no_sup_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if add_column_name is not None:
            self._values["add_column_name"] = add_column_name
        if bucket_folder is not None:
            self._values["bucket_folder"] = bucket_folder
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if canned_acl_for_objects is not None:
            self._values["canned_acl_for_objects"] = canned_acl_for_objects
        if cdc_inserts_and_updates is not None:
            self._values["cdc_inserts_and_updates"] = cdc_inserts_and_updates
        if cdc_inserts_only is not None:
            self._values["cdc_inserts_only"] = cdc_inserts_only
        if cdc_max_batch_interval is not None:
            self._values["cdc_max_batch_interval"] = cdc_max_batch_interval
        if cdc_min_file_size is not None:
            self._values["cdc_min_file_size"] = cdc_min_file_size
        if cdc_path is not None:
            self._values["cdc_path"] = cdc_path
        if compression_type is not None:
            self._values["compression_type"] = compression_type
        if csv_delimiter is not None:
            self._values["csv_delimiter"] = csv_delimiter
        if csv_no_sup_value is not None:
            self._values["csv_no_sup_value"] = csv_no_sup_value
        if csv_null_value is not None:
            self._values["csv_null_value"] = csv_null_value
        if csv_row_delimiter is not None:
            self._values["csv_row_delimiter"] = csv_row_delimiter
        if data_format is not None:
            self._values["data_format"] = data_format
        if data_page_size is not None:
            self._values["data_page_size"] = data_page_size
        if date_partition_delimiter is not None:
            self._values["date_partition_delimiter"] = date_partition_delimiter
        if date_partition_enabled is not None:
            self._values["date_partition_enabled"] = date_partition_enabled
        if date_partition_sequence is not None:
            self._values["date_partition_sequence"] = date_partition_sequence
        if dict_page_size_limit is not None:
            self._values["dict_page_size_limit"] = dict_page_size_limit
        if enable_statistics is not None:
            self._values["enable_statistics"] = enable_statistics
        if encoding_type is not None:
            self._values["encoding_type"] = encoding_type
        if encryption_mode is not None:
            self._values["encryption_mode"] = encryption_mode
        if external_table_definition is not None:
            self._values["external_table_definition"] = external_table_definition
        if ignore_headers_row is not None:
            self._values["ignore_headers_row"] = ignore_headers_row
        if include_op_for_full_load is not None:
            self._values["include_op_for_full_load"] = include_op_for_full_load
        if max_file_size is not None:
            self._values["max_file_size"] = max_file_size
        if parquet_timestamp_in_millisecond is not None:
            self._values["parquet_timestamp_in_millisecond"] = parquet_timestamp_in_millisecond
        if parquet_version is not None:
            self._values["parquet_version"] = parquet_version
        if preserve_transactions is not None:
            self._values["preserve_transactions"] = preserve_transactions
        if rfc4180 is not None:
            self._values["rfc4180"] = rfc4180
        if row_group_length is not None:
            self._values["row_group_length"] = row_group_length
        if server_side_encryption_kms_key_id is not None:
            self._values["server_side_encryption_kms_key_id"] = server_side_encryption_kms_key_id
        if service_access_role_arn is not None:
            self._values["service_access_role_arn"] = service_access_role_arn
        if timestamp_column_name is not None:
            self._values["timestamp_column_name"] = timestamp_column_name
        if use_csv_no_sup_value is not None:
            self._values["use_csv_no_sup_value"] = use_csv_no_sup_value

    @builtins.property
    def add_column_name(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#add_column_name DmsEndpoint#add_column_name}.'''
        result = self._values.get("add_column_name")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def bucket_folder(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_folder DmsEndpoint#bucket_folder}.'''
        result = self._values.get("bucket_folder")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_name DmsEndpoint#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def canned_acl_for_objects(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#canned_acl_for_objects DmsEndpoint#canned_acl_for_objects}.'''
        result = self._values.get("canned_acl_for_objects")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cdc_inserts_and_updates(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_inserts_and_updates DmsEndpoint#cdc_inserts_and_updates}.'''
        result = self._values.get("cdc_inserts_and_updates")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cdc_inserts_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_inserts_only DmsEndpoint#cdc_inserts_only}.'''
        result = self._values.get("cdc_inserts_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cdc_max_batch_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_max_batch_interval DmsEndpoint#cdc_max_batch_interval}.'''
        result = self._values.get("cdc_max_batch_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cdc_min_file_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_min_file_size DmsEndpoint#cdc_min_file_size}.'''
        result = self._values.get("cdc_min_file_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cdc_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_path DmsEndpoint#cdc_path}.'''
        result = self._values.get("cdc_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compression_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#compression_type DmsEndpoint#compression_type}.'''
        result = self._values.get("compression_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def csv_delimiter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_delimiter DmsEndpoint#csv_delimiter}.'''
        result = self._values.get("csv_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def csv_no_sup_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_no_sup_value DmsEndpoint#csv_no_sup_value}.'''
        result = self._values.get("csv_no_sup_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def csv_null_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_null_value DmsEndpoint#csv_null_value}.'''
        result = self._values.get("csv_null_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def csv_row_delimiter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_row_delimiter DmsEndpoint#csv_row_delimiter}.'''
        result = self._values.get("csv_row_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#data_format DmsEndpoint#data_format}.'''
        result = self._values.get("data_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_page_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#data_page_size DmsEndpoint#data_page_size}.'''
        result = self._values.get("data_page_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def date_partition_delimiter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_delimiter DmsEndpoint#date_partition_delimiter}.'''
        result = self._values.get("date_partition_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def date_partition_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_enabled DmsEndpoint#date_partition_enabled}.'''
        result = self._values.get("date_partition_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def date_partition_sequence(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_sequence DmsEndpoint#date_partition_sequence}.'''
        result = self._values.get("date_partition_sequence")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dict_page_size_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#dict_page_size_limit DmsEndpoint#dict_page_size_limit}.'''
        result = self._values.get("dict_page_size_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enable_statistics(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#enable_statistics DmsEndpoint#enable_statistics}.'''
        result = self._values.get("enable_statistics")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encoding_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encoding_type DmsEndpoint#encoding_type}.'''
        result = self._values.get("encoding_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encryption_mode DmsEndpoint#encryption_mode}.'''
        result = self._values.get("encryption_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_table_definition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#external_table_definition DmsEndpoint#external_table_definition}.'''
        result = self._values.get("external_table_definition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_headers_row(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ignore_headers_row DmsEndpoint#ignore_headers_row}.'''
        result = self._values.get("ignore_headers_row")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def include_op_for_full_load(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_op_for_full_load DmsEndpoint#include_op_for_full_load}.'''
        result = self._values.get("include_op_for_full_load")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_file_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#max_file_size DmsEndpoint#max_file_size}.'''
        result = self._values.get("max_file_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parquet_timestamp_in_millisecond(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#parquet_timestamp_in_millisecond DmsEndpoint#parquet_timestamp_in_millisecond}.'''
        result = self._values.get("parquet_timestamp_in_millisecond")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def parquet_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#parquet_version DmsEndpoint#parquet_version}.'''
        result = self._values.get("parquet_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preserve_transactions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#preserve_transactions DmsEndpoint#preserve_transactions}.'''
        result = self._values.get("preserve_transactions")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def rfc4180(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#rfc_4180 DmsEndpoint#rfc_4180}.'''
        result = self._values.get("rfc4180")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def row_group_length(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#row_group_length DmsEndpoint#row_group_length}.'''
        result = self._values.get("row_group_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def server_side_encryption_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_side_encryption_kms_key_id DmsEndpoint#server_side_encryption_kms_key_id}.'''
        result = self._values.get("server_side_encryption_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.'''
        result = self._values.get("service_access_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timestamp_column_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#timestamp_column_name DmsEndpoint#timestamp_column_name}.'''
        result = self._values.get("timestamp_column_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_csv_no_sup_value(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#use_csv_no_sup_value DmsEndpoint#use_csv_no_sup_value}.'''
        result = self._values.get("use_csv_no_sup_value")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointS3Settings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEndpointS3SettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dms.DmsEndpointS3SettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEndpointS3SettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAddColumnName")
    def reset_add_column_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddColumnName", []))

    @jsii.member(jsii_name="resetBucketFolder")
    def reset_bucket_folder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketFolder", []))

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetCannedAclForObjects")
    def reset_canned_acl_for_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCannedAclForObjects", []))

    @jsii.member(jsii_name="resetCdcInsertsAndUpdates")
    def reset_cdc_inserts_and_updates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdcInsertsAndUpdates", []))

    @jsii.member(jsii_name="resetCdcInsertsOnly")
    def reset_cdc_inserts_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdcInsertsOnly", []))

    @jsii.member(jsii_name="resetCdcMaxBatchInterval")
    def reset_cdc_max_batch_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdcMaxBatchInterval", []))

    @jsii.member(jsii_name="resetCdcMinFileSize")
    def reset_cdc_min_file_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdcMinFileSize", []))

    @jsii.member(jsii_name="resetCdcPath")
    def reset_cdc_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdcPath", []))

    @jsii.member(jsii_name="resetCompressionType")
    def reset_compression_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressionType", []))

    @jsii.member(jsii_name="resetCsvDelimiter")
    def reset_csv_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsvDelimiter", []))

    @jsii.member(jsii_name="resetCsvNoSupValue")
    def reset_csv_no_sup_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsvNoSupValue", []))

    @jsii.member(jsii_name="resetCsvNullValue")
    def reset_csv_null_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsvNullValue", []))

    @jsii.member(jsii_name="resetCsvRowDelimiter")
    def reset_csv_row_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsvRowDelimiter", []))

    @jsii.member(jsii_name="resetDataFormat")
    def reset_data_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataFormat", []))

    @jsii.member(jsii_name="resetDataPageSize")
    def reset_data_page_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataPageSize", []))

    @jsii.member(jsii_name="resetDatePartitionDelimiter")
    def reset_date_partition_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatePartitionDelimiter", []))

    @jsii.member(jsii_name="resetDatePartitionEnabled")
    def reset_date_partition_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatePartitionEnabled", []))

    @jsii.member(jsii_name="resetDatePartitionSequence")
    def reset_date_partition_sequence(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatePartitionSequence", []))

    @jsii.member(jsii_name="resetDictPageSizeLimit")
    def reset_dict_page_size_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDictPageSizeLimit", []))

    @jsii.member(jsii_name="resetEnableStatistics")
    def reset_enable_statistics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableStatistics", []))

    @jsii.member(jsii_name="resetEncodingType")
    def reset_encoding_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncodingType", []))

    @jsii.member(jsii_name="resetEncryptionMode")
    def reset_encryption_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionMode", []))

    @jsii.member(jsii_name="resetExternalTableDefinition")
    def reset_external_table_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalTableDefinition", []))

    @jsii.member(jsii_name="resetIgnoreHeadersRow")
    def reset_ignore_headers_row(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreHeadersRow", []))

    @jsii.member(jsii_name="resetIncludeOpForFullLoad")
    def reset_include_op_for_full_load(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeOpForFullLoad", []))

    @jsii.member(jsii_name="resetMaxFileSize")
    def reset_max_file_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxFileSize", []))

    @jsii.member(jsii_name="resetParquetTimestampInMillisecond")
    def reset_parquet_timestamp_in_millisecond(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParquetTimestampInMillisecond", []))

    @jsii.member(jsii_name="resetParquetVersion")
    def reset_parquet_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParquetVersion", []))

    @jsii.member(jsii_name="resetPreserveTransactions")
    def reset_preserve_transactions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreserveTransactions", []))

    @jsii.member(jsii_name="resetRfc4180")
    def reset_rfc4180(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRfc4180", []))

    @jsii.member(jsii_name="resetRowGroupLength")
    def reset_row_group_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRowGroupLength", []))

    @jsii.member(jsii_name="resetServerSideEncryptionKmsKeyId")
    def reset_server_side_encryption_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerSideEncryptionKmsKeyId", []))

    @jsii.member(jsii_name="resetServiceAccessRoleArn")
    def reset_service_access_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccessRoleArn", []))

    @jsii.member(jsii_name="resetTimestampColumnName")
    def reset_timestamp_column_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimestampColumnName", []))

    @jsii.member(jsii_name="resetUseCsvNoSupValue")
    def reset_use_csv_no_sup_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCsvNoSupValue", []))

    @builtins.property
    @jsii.member(jsii_name="addColumnNameInput")
    def add_column_name_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "addColumnNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketFolderInput")
    def bucket_folder_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketFolderInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cannedAclForObjectsInput")
    def canned_acl_for_objects_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cannedAclForObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="cdcInsertsAndUpdatesInput")
    def cdc_inserts_and_updates_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cdcInsertsAndUpdatesInput"))

    @builtins.property
    @jsii.member(jsii_name="cdcInsertsOnlyInput")
    def cdc_inserts_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cdcInsertsOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="cdcMaxBatchIntervalInput")
    def cdc_max_batch_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cdcMaxBatchIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="cdcMinFileSizeInput")
    def cdc_min_file_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cdcMinFileSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="cdcPathInput")
    def cdc_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdcPathInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionTypeInput")
    def compression_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="csvDelimiterInput")
    def csv_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "csvDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="csvNoSupValueInput")
    def csv_no_sup_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "csvNoSupValueInput"))

    @builtins.property
    @jsii.member(jsii_name="csvNullValueInput")
    def csv_null_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "csvNullValueInput"))

    @builtins.property
    @jsii.member(jsii_name="csvRowDelimiterInput")
    def csv_row_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "csvRowDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFormatInput")
    def data_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="dataPageSizeInput")
    def data_page_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataPageSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="datePartitionDelimiterInput")
    def date_partition_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datePartitionDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="datePartitionEnabledInput")
    def date_partition_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "datePartitionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="datePartitionSequenceInput")
    def date_partition_sequence_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datePartitionSequenceInput"))

    @builtins.property
    @jsii.member(jsii_name="dictPageSizeLimitInput")
    def dict_page_size_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dictPageSizeLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="enableStatisticsInput")
    def enable_statistics_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableStatisticsInput"))

    @builtins.property
    @jsii.member(jsii_name="encodingTypeInput")
    def encoding_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encodingTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionModeInput")
    def encryption_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="externalTableDefinitionInput")
    def external_table_definition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalTableDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreHeadersRowInput")
    def ignore_headers_row_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ignoreHeadersRowInput"))

    @builtins.property
    @jsii.member(jsii_name="includeOpForFullLoadInput")
    def include_op_for_full_load_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeOpForFullLoadInput"))

    @builtins.property
    @jsii.member(jsii_name="maxFileSizeInput")
    def max_file_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxFileSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="parquetTimestampInMillisecondInput")
    def parquet_timestamp_in_millisecond_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "parquetTimestampInMillisecondInput"))

    @builtins.property
    @jsii.member(jsii_name="parquetVersionInput")
    def parquet_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parquetVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="preserveTransactionsInput")
    def preserve_transactions_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preserveTransactionsInput"))

    @builtins.property
    @jsii.member(jsii_name="rfc4180Input")
    def rfc4180_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "rfc4180Input"))

    @builtins.property
    @jsii.member(jsii_name="rowGroupLengthInput")
    def row_group_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowGroupLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionKmsKeyIdInput")
    def server_side_encryption_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverSideEncryptionKmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArnInput")
    def service_access_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccessRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="timestampColumnNameInput")
    def timestamp_column_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timestampColumnNameInput"))

    @builtins.property
    @jsii.member(jsii_name="useCsvNoSupValueInput")
    def use_csv_no_sup_value_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useCsvNoSupValueInput"))

    @builtins.property
    @jsii.member(jsii_name="addColumnName")
    def add_column_name(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "addColumnName"))

    @add_column_name.setter
    def add_column_name(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "add_column_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addColumnName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketFolder")
    def bucket_folder(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketFolder"))

    @bucket_folder.setter
    def bucket_folder(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "bucket_folder").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketFolder", value)

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "bucket_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="cannedAclForObjects")
    def canned_acl_for_objects(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cannedAclForObjects"))

    @canned_acl_for_objects.setter
    def canned_acl_for_objects(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "canned_acl_for_objects").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cannedAclForObjects", value)

    @builtins.property
    @jsii.member(jsii_name="cdcInsertsAndUpdates")
    def cdc_inserts_and_updates(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cdcInsertsAndUpdates"))

    @cdc_inserts_and_updates.setter
    def cdc_inserts_and_updates(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "cdc_inserts_and_updates").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcInsertsAndUpdates", value)

    @builtins.property
    @jsii.member(jsii_name="cdcInsertsOnly")
    def cdc_inserts_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cdcInsertsOnly"))

    @cdc_inserts_only.setter
    def cdc_inserts_only(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "cdc_inserts_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcInsertsOnly", value)

    @builtins.property
    @jsii.member(jsii_name="cdcMaxBatchInterval")
    def cdc_max_batch_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cdcMaxBatchInterval"))

    @cdc_max_batch_interval.setter
    def cdc_max_batch_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "cdc_max_batch_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcMaxBatchInterval", value)

    @builtins.property
    @jsii.member(jsii_name="cdcMinFileSize")
    def cdc_min_file_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cdcMinFileSize"))

    @cdc_min_file_size.setter
    def cdc_min_file_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "cdc_min_file_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcMinFileSize", value)

    @builtins.property
    @jsii.member(jsii_name="cdcPath")
    def cdc_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdcPath"))

    @cdc_path.setter
    def cdc_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "cdc_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcPath", value)

    @builtins.property
    @jsii.member(jsii_name="compressionType")
    def compression_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compressionType"))

    @compression_type.setter
    def compression_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "compression_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressionType", value)

    @builtins.property
    @jsii.member(jsii_name="csvDelimiter")
    def csv_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csvDelimiter"))

    @csv_delimiter.setter
    def csv_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "csv_delimiter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="csvNoSupValue")
    def csv_no_sup_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csvNoSupValue"))

    @csv_no_sup_value.setter
    def csv_no_sup_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "csv_no_sup_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvNoSupValue", value)

    @builtins.property
    @jsii.member(jsii_name="csvNullValue")
    def csv_null_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csvNullValue"))

    @csv_null_value.setter
    def csv_null_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "csv_null_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvNullValue", value)

    @builtins.property
    @jsii.member(jsii_name="csvRowDelimiter")
    def csv_row_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csvRowDelimiter"))

    @csv_row_delimiter.setter
    def csv_row_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "csv_row_delimiter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvRowDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="dataFormat")
    def data_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataFormat"))

    @data_format.setter
    def data_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "data_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFormat", value)

    @builtins.property
    @jsii.member(jsii_name="dataPageSize")
    def data_page_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dataPageSize"))

    @data_page_size.setter
    def data_page_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "data_page_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataPageSize", value)

    @builtins.property
    @jsii.member(jsii_name="datePartitionDelimiter")
    def date_partition_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datePartitionDelimiter"))

    @date_partition_delimiter.setter
    def date_partition_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "date_partition_delimiter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datePartitionDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="datePartitionEnabled")
    def date_partition_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "datePartitionEnabled"))

    @date_partition_enabled.setter
    def date_partition_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "date_partition_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datePartitionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="datePartitionSequence")
    def date_partition_sequence(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datePartitionSequence"))

    @date_partition_sequence.setter
    def date_partition_sequence(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "date_partition_sequence").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datePartitionSequence", value)

    @builtins.property
    @jsii.member(jsii_name="dictPageSizeLimit")
    def dict_page_size_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dictPageSizeLimit"))

    @dict_page_size_limit.setter
    def dict_page_size_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "dict_page_size_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dictPageSizeLimit", value)

    @builtins.property
    @jsii.member(jsii_name="enableStatistics")
    def enable_statistics(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableStatistics"))

    @enable_statistics.setter
    def enable_statistics(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "enable_statistics").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableStatistics", value)

    @builtins.property
    @jsii.member(jsii_name="encodingType")
    def encoding_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encodingType"))

    @encoding_type.setter
    def encoding_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "encoding_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encodingType", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionMode")
    def encryption_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionMode"))

    @encryption_mode.setter
    def encryption_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "encryption_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionMode", value)

    @builtins.property
    @jsii.member(jsii_name="externalTableDefinition")
    def external_table_definition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalTableDefinition"))

    @external_table_definition.setter
    def external_table_definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "external_table_definition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalTableDefinition", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreHeadersRow")
    def ignore_headers_row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ignoreHeadersRow"))

    @ignore_headers_row.setter
    def ignore_headers_row(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "ignore_headers_row").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreHeadersRow", value)

    @builtins.property
    @jsii.member(jsii_name="includeOpForFullLoad")
    def include_op_for_full_load(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeOpForFullLoad"))

    @include_op_for_full_load.setter
    def include_op_for_full_load(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "include_op_for_full_load").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeOpForFullLoad", value)

    @builtins.property
    @jsii.member(jsii_name="maxFileSize")
    def max_file_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxFileSize"))

    @max_file_size.setter
    def max_file_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "max_file_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxFileSize", value)

    @builtins.property
    @jsii.member(jsii_name="parquetTimestampInMillisecond")
    def parquet_timestamp_in_millisecond(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "parquetTimestampInMillisecond"))

    @parquet_timestamp_in_millisecond.setter
    def parquet_timestamp_in_millisecond(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "parquet_timestamp_in_millisecond").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parquetTimestampInMillisecond", value)

    @builtins.property
    @jsii.member(jsii_name="parquetVersion")
    def parquet_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parquetVersion"))

    @parquet_version.setter
    def parquet_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "parquet_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parquetVersion", value)

    @builtins.property
    @jsii.member(jsii_name="preserveTransactions")
    def preserve_transactions(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preserveTransactions"))

    @preserve_transactions.setter
    def preserve_transactions(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "preserve_transactions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preserveTransactions", value)

    @builtins.property
    @jsii.member(jsii_name="rfc4180")
    def rfc4180(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "rfc4180"))

    @rfc4180.setter
    def rfc4180(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "rfc4180").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rfc4180", value)

    @builtins.property
    @jsii.member(jsii_name="rowGroupLength")
    def row_group_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rowGroupLength"))

    @row_group_length.setter
    def row_group_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "row_group_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rowGroupLength", value)

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionKmsKeyId")
    def server_side_encryption_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverSideEncryptionKmsKeyId"))

    @server_side_encryption_kms_key_id.setter
    def server_side_encryption_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "server_side_encryption_kms_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideEncryptionKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessRoleArn"))

    @service_access_role_arn.setter
    def service_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "service_access_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="timestampColumnName")
    def timestamp_column_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timestampColumnName"))

    @timestamp_column_name.setter
    def timestamp_column_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "timestamp_column_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timestampColumnName", value)

    @builtins.property
    @jsii.member(jsii_name="useCsvNoSupValue")
    def use_csv_no_sup_value(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useCsvNoSupValue"))

    @use_csv_no_sup_value.setter
    def use_csv_no_sup_value(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "use_csv_no_sup_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCsvNoSupValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DmsEndpointS3Settings]:
        return typing.cast(typing.Optional[DmsEndpointS3Settings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DmsEndpointS3Settings]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointS3SettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dms.DmsEndpointTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class DmsEndpointTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#create DmsEndpoint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#delete DmsEndpoint#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEndpointTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#create DmsEndpoint#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#delete DmsEndpoint#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEndpointTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dms.DmsEndpointTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEndpointTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DmsEndpointTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DmsEndpointTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DmsEndpointTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEndpointTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DmsEventSubscription(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dms.DmsEventSubscription",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription aws_dms_event_subscription}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        event_categories: typing.Sequence[builtins.str],
        name: builtins.str,
        sns_topic_arn: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DmsEventSubscriptionTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription aws_dms_event_subscription} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param event_categories: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#event_categories DmsEventSubscription#event_categories}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#name DmsEventSubscription#name}.
        :param sns_topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#sns_topic_arn DmsEventSubscription#sns_topic_arn}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#enabled DmsEventSubscription#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#id DmsEventSubscription#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param source_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#source_ids DmsEventSubscription#source_ids}.
        :param source_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#source_type DmsEventSubscription#source_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#tags DmsEventSubscription#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#tags_all DmsEventSubscription#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#timeouts DmsEventSubscription#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEventSubscription.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DmsEventSubscriptionConfig(
            event_categories=event_categories,
            name=name,
            sns_topic_arn=sns_topic_arn,
            enabled=enabled,
            id=id,
            source_ids=source_ids,
            source_type=source_type,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#create DmsEventSubscription#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#delete DmsEventSubscription#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#update DmsEventSubscription#update}.
        '''
        value = DmsEventSubscriptionTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSourceIds")
    def reset_source_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceIds", []))

    @jsii.member(jsii_name="resetSourceType")
    def reset_source_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceType", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DmsEventSubscriptionTimeoutsOutputReference":
        return typing.cast("DmsEventSubscriptionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="eventCategoriesInput")
    def event_categories_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventCategoriesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="snsTopicArnInput")
    def sns_topic_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snsTopicArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIdsInput")
    def source_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceTypeInput")
    def source_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DmsEventSubscriptionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DmsEventSubscriptionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEventSubscription, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="eventCategories")
    def event_categories(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "eventCategories"))

    @event_categories.setter
    def event_categories(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEventSubscription, "event_categories").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventCategories", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEventSubscription, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEventSubscription, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snsTopicArn"))

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEventSubscription, "sns_topic_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIds")
    def source_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceIds"))

    @source_ids.setter
    def source_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEventSubscription, "source_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIds", value)

    @builtins.property
    @jsii.member(jsii_name="sourceType")
    def source_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceType"))

    @source_type.setter
    def source_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEventSubscription, "source_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEventSubscription, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEventSubscription, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dms.DmsEventSubscriptionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "event_categories": "eventCategories",
        "name": "name",
        "sns_topic_arn": "snsTopicArn",
        "enabled": "enabled",
        "id": "id",
        "source_ids": "sourceIds",
        "source_type": "sourceType",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class DmsEventSubscriptionConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        event_categories: typing.Sequence[builtins.str],
        name: builtins.str,
        sns_topic_arn: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DmsEventSubscriptionTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''AWS Database Migration Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param event_categories: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#event_categories DmsEventSubscription#event_categories}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#name DmsEventSubscription#name}.
        :param sns_topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#sns_topic_arn DmsEventSubscription#sns_topic_arn}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#enabled DmsEventSubscription#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#id DmsEventSubscription#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param source_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#source_ids DmsEventSubscription#source_ids}.
        :param source_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#source_type DmsEventSubscription#source_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#tags DmsEventSubscription#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#tags_all DmsEventSubscription#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#timeouts DmsEventSubscription#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DmsEventSubscriptionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DmsEventSubscriptionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument event_categories", value=event_categories, expected_type=type_hints["event_categories"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument source_ids", value=source_ids, expected_type=type_hints["source_ids"])
            check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "event_categories": event_categories,
            "name": name,
            "sns_topic_arn": sns_topic_arn,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if source_ids is not None:
            self._values["source_ids"] = source_ids
        if source_type is not None:
            self._values["source_type"] = source_type
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def event_categories(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#event_categories DmsEventSubscription#event_categories}.'''
        result = self._values.get("event_categories")
        assert result is not None, "Required property 'event_categories' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#name DmsEventSubscription#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sns_topic_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#sns_topic_arn DmsEventSubscription#sns_topic_arn}.'''
        result = self._values.get("sns_topic_arn")
        assert result is not None, "Required property 'sns_topic_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#enabled DmsEventSubscription#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#id DmsEventSubscription#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#source_ids DmsEventSubscription#source_ids}.'''
        result = self._values.get("source_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#source_type DmsEventSubscription#source_type}.'''
        result = self._values.get("source_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#tags DmsEventSubscription#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#tags_all DmsEventSubscription#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DmsEventSubscriptionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#timeouts DmsEventSubscription#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DmsEventSubscriptionTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEventSubscriptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dms.DmsEventSubscriptionTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class DmsEventSubscriptionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#create DmsEventSubscription#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#delete DmsEventSubscription#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#update DmsEventSubscription#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEventSubscriptionTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#create DmsEventSubscription#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#delete DmsEventSubscription#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_event_subscription#update DmsEventSubscription#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEventSubscriptionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEventSubscriptionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dms.DmsEventSubscriptionTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsEventSubscriptionTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEventSubscriptionTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEventSubscriptionTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEventSubscriptionTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DmsEventSubscriptionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DmsEventSubscriptionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DmsEventSubscriptionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsEventSubscriptionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DmsReplicationInstance(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dms.DmsReplicationInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance aws_dms_replication_instance}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        replication_instance_class: builtins.str,
        replication_instance_id: builtins.str,
        allocated_storage: typing.Optional[jsii.Number] = None,
        allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        apply_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        multi_az: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        replication_subnet_group_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DmsReplicationInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance aws_dms_replication_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param replication_instance_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#replication_instance_class DmsReplicationInstance#replication_instance_class}.
        :param replication_instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#replication_instance_id DmsReplicationInstance#replication_instance_id}.
        :param allocated_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#allocated_storage DmsReplicationInstance#allocated_storage}.
        :param allow_major_version_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#allow_major_version_upgrade DmsReplicationInstance#allow_major_version_upgrade}.
        :param apply_immediately: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#apply_immediately DmsReplicationInstance#apply_immediately}.
        :param auto_minor_version_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#auto_minor_version_upgrade DmsReplicationInstance#auto_minor_version_upgrade}.
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#availability_zone DmsReplicationInstance#availability_zone}.
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#engine_version DmsReplicationInstance#engine_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#id DmsReplicationInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#kms_key_arn DmsReplicationInstance#kms_key_arn}.
        :param multi_az: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#multi_az DmsReplicationInstance#multi_az}.
        :param preferred_maintenance_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#preferred_maintenance_window DmsReplicationInstance#preferred_maintenance_window}.
        :param publicly_accessible: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#publicly_accessible DmsReplicationInstance#publicly_accessible}.
        :param replication_subnet_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#replication_subnet_group_id DmsReplicationInstance#replication_subnet_group_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#tags DmsReplicationInstance#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#tags_all DmsReplicationInstance#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#timeouts DmsReplicationInstance#timeouts}
        :param vpc_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#vpc_security_group_ids DmsReplicationInstance#vpc_security_group_ids}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsReplicationInstance.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DmsReplicationInstanceConfig(
            replication_instance_class=replication_instance_class,
            replication_instance_id=replication_instance_id,
            allocated_storage=allocated_storage,
            allow_major_version_upgrade=allow_major_version_upgrade,
            apply_immediately=apply_immediately,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            availability_zone=availability_zone,
            engine_version=engine_version,
            id=id,
            kms_key_arn=kms_key_arn,
            multi_az=multi_az,
            preferred_maintenance_window=preferred_maintenance_window,
            publicly_accessible=publicly_accessible,
            replication_subnet_group_id=replication_subnet_group_id,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            vpc_security_group_ids=vpc_security_group_ids,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#create DmsReplicationInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#delete DmsReplicationInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#update DmsReplicationInstance#update}.
        '''
        value = DmsReplicationInstanceTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAllocatedStorage")
    def reset_allocated_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllocatedStorage", []))

    @jsii.member(jsii_name="resetAllowMajorVersionUpgrade")
    def reset_allow_major_version_upgrade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowMajorVersionUpgrade", []))

    @jsii.member(jsii_name="resetApplyImmediately")
    def reset_apply_immediately(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplyImmediately", []))

    @jsii.member(jsii_name="resetAutoMinorVersionUpgrade")
    def reset_auto_minor_version_upgrade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoMinorVersionUpgrade", []))

    @jsii.member(jsii_name="resetAvailabilityZone")
    def reset_availability_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZone", []))

    @jsii.member(jsii_name="resetEngineVersion")
    def reset_engine_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEngineVersion", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetMultiAz")
    def reset_multi_az(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultiAz", []))

    @jsii.member(jsii_name="resetPreferredMaintenanceWindow")
    def reset_preferred_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredMaintenanceWindow", []))

    @jsii.member(jsii_name="resetPubliclyAccessible")
    def reset_publicly_accessible(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPubliclyAccessible", []))

    @jsii.member(jsii_name="resetReplicationSubnetGroupId")
    def reset_replication_subnet_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicationSubnetGroupId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVpcSecurityGroupIds")
    def reset_vpc_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcSecurityGroupIds", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="replicationInstanceArn")
    def replication_instance_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationInstanceArn"))

    @builtins.property
    @jsii.member(jsii_name="replicationInstancePrivateIps")
    def replication_instance_private_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "replicationInstancePrivateIps"))

    @builtins.property
    @jsii.member(jsii_name="replicationInstancePublicIps")
    def replication_instance_public_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "replicationInstancePublicIps"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DmsReplicationInstanceTimeoutsOutputReference":
        return typing.cast("DmsReplicationInstanceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="allocatedStorageInput")
    def allocated_storage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "allocatedStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="allowMajorVersionUpgradeInput")
    def allow_major_version_upgrade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowMajorVersionUpgradeInput"))

    @builtins.property
    @jsii.member(jsii_name="applyImmediatelyInput")
    def apply_immediately_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "applyImmediatelyInput"))

    @builtins.property
    @jsii.member(jsii_name="autoMinorVersionUpgradeInput")
    def auto_minor_version_upgrade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoMinorVersionUpgradeInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneInput")
    def availability_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="engineVersionInput")
    def engine_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="multiAzInput")
    def multi_az_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "multiAzInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindowInput")
    def preferred_maintenance_window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessibleInput")
    def publicly_accessible_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publiclyAccessibleInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationInstanceClassInput")
    def replication_instance_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationInstanceClassInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationInstanceIdInput")
    def replication_instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationInstanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationSubnetGroupIdInput")
    def replication_subnet_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationSubnetGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DmsReplicationInstanceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DmsReplicationInstanceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIdsInput")
    def vpc_security_group_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="allocatedStorage")
    def allocated_storage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "allocatedStorage"))

    @allocated_storage.setter
    def allocated_storage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "allocated_storage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocatedStorage", value)

    @builtins.property
    @jsii.member(jsii_name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowMajorVersionUpgrade"))

    @allow_major_version_upgrade.setter
    def allow_major_version_upgrade(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "allow_major_version_upgrade").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMajorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="applyImmediately")
    def apply_immediately(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "applyImmediately"))

    @apply_immediately.setter
    def apply_immediately(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "apply_immediately").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyImmediately", value)

    @builtins.property
    @jsii.member(jsii_name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoMinorVersionUpgrade"))

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "auto_minor_version_upgrade").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoMinorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "availability_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "engine_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "kms_key_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="multiAz")
    def multi_az(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "multiAz"))

    @multi_az.setter
    def multi_az(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "multi_az").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multiAz", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "preferred_maintenance_window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publiclyAccessible"))

    @publicly_accessible.setter
    def publicly_accessible(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "publicly_accessible").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publiclyAccessible", value)

    @builtins.property
    @jsii.member(jsii_name="replicationInstanceClass")
    def replication_instance_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationInstanceClass"))

    @replication_instance_class.setter
    def replication_instance_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "replication_instance_class").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationInstanceClass", value)

    @builtins.property
    @jsii.member(jsii_name="replicationInstanceId")
    def replication_instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationInstanceId"))

    @replication_instance_id.setter
    def replication_instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "replication_instance_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationInstanceId", value)

    @builtins.property
    @jsii.member(jsii_name="replicationSubnetGroupId")
    def replication_subnet_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationSubnetGroupId"))

    @replication_subnet_group_id.setter
    def replication_subnet_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "replication_subnet_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationSubnetGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstance, "vpc_security_group_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dms.DmsReplicationInstanceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "replication_instance_class": "replicationInstanceClass",
        "replication_instance_id": "replicationInstanceId",
        "allocated_storage": "allocatedStorage",
        "allow_major_version_upgrade": "allowMajorVersionUpgrade",
        "apply_immediately": "applyImmediately",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "availability_zone": "availabilityZone",
        "engine_version": "engineVersion",
        "id": "id",
        "kms_key_arn": "kmsKeyArn",
        "multi_az": "multiAz",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "publicly_accessible": "publiclyAccessible",
        "replication_subnet_group_id": "replicationSubnetGroupId",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class DmsReplicationInstanceConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        replication_instance_class: builtins.str,
        replication_instance_id: builtins.str,
        allocated_storage: typing.Optional[jsii.Number] = None,
        allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        apply_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        multi_az: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        replication_subnet_group_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DmsReplicationInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''AWS Database Migration Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param replication_instance_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#replication_instance_class DmsReplicationInstance#replication_instance_class}.
        :param replication_instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#replication_instance_id DmsReplicationInstance#replication_instance_id}.
        :param allocated_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#allocated_storage DmsReplicationInstance#allocated_storage}.
        :param allow_major_version_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#allow_major_version_upgrade DmsReplicationInstance#allow_major_version_upgrade}.
        :param apply_immediately: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#apply_immediately DmsReplicationInstance#apply_immediately}.
        :param auto_minor_version_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#auto_minor_version_upgrade DmsReplicationInstance#auto_minor_version_upgrade}.
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#availability_zone DmsReplicationInstance#availability_zone}.
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#engine_version DmsReplicationInstance#engine_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#id DmsReplicationInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#kms_key_arn DmsReplicationInstance#kms_key_arn}.
        :param multi_az: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#multi_az DmsReplicationInstance#multi_az}.
        :param preferred_maintenance_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#preferred_maintenance_window DmsReplicationInstance#preferred_maintenance_window}.
        :param publicly_accessible: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#publicly_accessible DmsReplicationInstance#publicly_accessible}.
        :param replication_subnet_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#replication_subnet_group_id DmsReplicationInstance#replication_subnet_group_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#tags DmsReplicationInstance#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#tags_all DmsReplicationInstance#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#timeouts DmsReplicationInstance#timeouts}
        :param vpc_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#vpc_security_group_ids DmsReplicationInstance#vpc_security_group_ids}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DmsReplicationInstanceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DmsReplicationInstanceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument replication_instance_class", value=replication_instance_class, expected_type=type_hints["replication_instance_class"])
            check_type(argname="argument replication_instance_id", value=replication_instance_id, expected_type=type_hints["replication_instance_id"])
            check_type(argname="argument allocated_storage", value=allocated_storage, expected_type=type_hints["allocated_storage"])
            check_type(argname="argument allow_major_version_upgrade", value=allow_major_version_upgrade, expected_type=type_hints["allow_major_version_upgrade"])
            check_type(argname="argument apply_immediately", value=apply_immediately, expected_type=type_hints["apply_immediately"])
            check_type(argname="argument auto_minor_version_upgrade", value=auto_minor_version_upgrade, expected_type=type_hints["auto_minor_version_upgrade"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument multi_az", value=multi_az, expected_type=type_hints["multi_az"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
            check_type(argname="argument replication_subnet_group_id", value=replication_subnet_group_id, expected_type=type_hints["replication_subnet_group_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "replication_instance_class": replication_instance_class,
            "replication_instance_id": replication_instance_id,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if allocated_storage is not None:
            self._values["allocated_storage"] = allocated_storage
        if allow_major_version_upgrade is not None:
            self._values["allow_major_version_upgrade"] = allow_major_version_upgrade
        if apply_immediately is not None:
            self._values["apply_immediately"] = apply_immediately
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if id is not None:
            self._values["id"] = id
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if multi_az is not None:
            self._values["multi_az"] = multi_az
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if publicly_accessible is not None:
            self._values["publicly_accessible"] = publicly_accessible
        if replication_subnet_group_id is not None:
            self._values["replication_subnet_group_id"] = replication_subnet_group_id
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def replication_instance_class(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#replication_instance_class DmsReplicationInstance#replication_instance_class}.'''
        result = self._values.get("replication_instance_class")
        assert result is not None, "Required property 'replication_instance_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replication_instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#replication_instance_id DmsReplicationInstance#replication_instance_id}.'''
        result = self._values.get("replication_instance_id")
        assert result is not None, "Required property 'replication_instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allocated_storage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#allocated_storage DmsReplicationInstance#allocated_storage}.'''
        result = self._values.get("allocated_storage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def allow_major_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#allow_major_version_upgrade DmsReplicationInstance#allow_major_version_upgrade}.'''
        result = self._values.get("allow_major_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def apply_immediately(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#apply_immediately DmsReplicationInstance#apply_immediately}.'''
        result = self._values.get("apply_immediately")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#auto_minor_version_upgrade DmsReplicationInstance#auto_minor_version_upgrade}.'''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#availability_zone DmsReplicationInstance#availability_zone}.'''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#engine_version DmsReplicationInstance#engine_version}.'''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#id DmsReplicationInstance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#kms_key_arn DmsReplicationInstance#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multi_az(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#multi_az DmsReplicationInstance#multi_az}.'''
        result = self._values.get("multi_az")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#preferred_maintenance_window DmsReplicationInstance#preferred_maintenance_window}.'''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#publicly_accessible DmsReplicationInstance#publicly_accessible}.'''
        result = self._values.get("publicly_accessible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def replication_subnet_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#replication_subnet_group_id DmsReplicationInstance#replication_subnet_group_id}.'''
        result = self._values.get("replication_subnet_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#tags DmsReplicationInstance#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#tags_all DmsReplicationInstance#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DmsReplicationInstanceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#timeouts DmsReplicationInstance#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DmsReplicationInstanceTimeouts"], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#vpc_security_group_ids DmsReplicationInstance#vpc_security_group_ids}.'''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsReplicationInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dms.DmsReplicationInstanceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class DmsReplicationInstanceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#create DmsReplicationInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#delete DmsReplicationInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#update DmsReplicationInstance#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsReplicationInstanceTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#create DmsReplicationInstance#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#delete DmsReplicationInstance#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_instance#update DmsReplicationInstance#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsReplicationInstanceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsReplicationInstanceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dms.DmsReplicationInstanceTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsReplicationInstanceTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstanceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstanceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstanceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DmsReplicationInstanceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DmsReplicationInstanceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DmsReplicationInstanceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationInstanceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DmsReplicationSubnetGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dms.DmsReplicationSubnetGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group aws_dms_replication_subnet_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        replication_subnet_group_description: builtins.str,
        replication_subnet_group_id: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group aws_dms_replication_subnet_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param replication_subnet_group_description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#replication_subnet_group_description DmsReplicationSubnetGroup#replication_subnet_group_description}.
        :param replication_subnet_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#replication_subnet_group_id DmsReplicationSubnetGroup#replication_subnet_group_id}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#subnet_ids DmsReplicationSubnetGroup#subnet_ids}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#id DmsReplicationSubnetGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#tags DmsReplicationSubnetGroup#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#tags_all DmsReplicationSubnetGroup#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsReplicationSubnetGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DmsReplicationSubnetGroupConfig(
            replication_subnet_group_description=replication_subnet_group_description,
            replication_subnet_group_id=replication_subnet_group_id,
            subnet_ids=subnet_ids,
            id=id,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="replicationSubnetGroupArn")
    def replication_subnet_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationSubnetGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationSubnetGroupDescriptionInput")
    def replication_subnet_group_description_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationSubnetGroupDescriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationSubnetGroupIdInput")
    def replication_subnet_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationSubnetGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationSubnetGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="replicationSubnetGroupDescription")
    def replication_subnet_group_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationSubnetGroupDescription"))

    @replication_subnet_group_description.setter
    def replication_subnet_group_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationSubnetGroup, "replication_subnet_group_description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationSubnetGroupDescription", value)

    @builtins.property
    @jsii.member(jsii_name="replicationSubnetGroupId")
    def replication_subnet_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationSubnetGroupId"))

    @replication_subnet_group_id.setter
    def replication_subnet_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationSubnetGroup, "replication_subnet_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationSubnetGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationSubnetGroup, "subnet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationSubnetGroup, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationSubnetGroup, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dms.DmsReplicationSubnetGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "replication_subnet_group_description": "replicationSubnetGroupDescription",
        "replication_subnet_group_id": "replicationSubnetGroupId",
        "subnet_ids": "subnetIds",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class DmsReplicationSubnetGroupConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        replication_subnet_group_description: builtins.str,
        replication_subnet_group_id: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS Database Migration Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param replication_subnet_group_description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#replication_subnet_group_description DmsReplicationSubnetGroup#replication_subnet_group_description}.
        :param replication_subnet_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#replication_subnet_group_id DmsReplicationSubnetGroup#replication_subnet_group_id}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#subnet_ids DmsReplicationSubnetGroup#subnet_ids}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#id DmsReplicationSubnetGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#tags DmsReplicationSubnetGroup#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#tags_all DmsReplicationSubnetGroup#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DmsReplicationSubnetGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument replication_subnet_group_description", value=replication_subnet_group_description, expected_type=type_hints["replication_subnet_group_description"])
            check_type(argname="argument replication_subnet_group_id", value=replication_subnet_group_id, expected_type=type_hints["replication_subnet_group_id"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "replication_subnet_group_description": replication_subnet_group_description,
            "replication_subnet_group_id": replication_subnet_group_id,
            "subnet_ids": subnet_ids,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def replication_subnet_group_description(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#replication_subnet_group_description DmsReplicationSubnetGroup#replication_subnet_group_description}.'''
        result = self._values.get("replication_subnet_group_description")
        assert result is not None, "Required property 'replication_subnet_group_description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replication_subnet_group_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#replication_subnet_group_id DmsReplicationSubnetGroup#replication_subnet_group_id}.'''
        result = self._values.get("replication_subnet_group_id")
        assert result is not None, "Required property 'replication_subnet_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#subnet_ids DmsReplicationSubnetGroup#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#id DmsReplicationSubnetGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#tags DmsReplicationSubnetGroup#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group#tags_all DmsReplicationSubnetGroup#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsReplicationSubnetGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsReplicationTask(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dms.DmsReplicationTask",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task aws_dms_replication_task}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        migration_type: builtins.str,
        replication_instance_arn: builtins.str,
        replication_task_id: builtins.str,
        source_endpoint_arn: builtins.str,
        table_mappings: builtins.str,
        target_endpoint_arn: builtins.str,
        cdc_start_position: typing.Optional[builtins.str] = None,
        cdc_start_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        replication_task_settings: typing.Optional[builtins.str] = None,
        start_replication_task: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task aws_dms_replication_task} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param migration_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#migration_type DmsReplicationTask#migration_type}.
        :param replication_instance_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_instance_arn DmsReplicationTask#replication_instance_arn}.
        :param replication_task_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_task_id DmsReplicationTask#replication_task_id}.
        :param source_endpoint_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#source_endpoint_arn DmsReplicationTask#source_endpoint_arn}.
        :param table_mappings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#table_mappings DmsReplicationTask#table_mappings}.
        :param target_endpoint_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#target_endpoint_arn DmsReplicationTask#target_endpoint_arn}.
        :param cdc_start_position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#cdc_start_position DmsReplicationTask#cdc_start_position}.
        :param cdc_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#cdc_start_time DmsReplicationTask#cdc_start_time}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#id DmsReplicationTask#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param replication_task_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_task_settings DmsReplicationTask#replication_task_settings}.
        :param start_replication_task: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#start_replication_task DmsReplicationTask#start_replication_task}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#tags DmsReplicationTask#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#tags_all DmsReplicationTask#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DmsReplicationTask.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DmsReplicationTaskConfig(
            migration_type=migration_type,
            replication_instance_arn=replication_instance_arn,
            replication_task_id=replication_task_id,
            source_endpoint_arn=source_endpoint_arn,
            table_mappings=table_mappings,
            target_endpoint_arn=target_endpoint_arn,
            cdc_start_position=cdc_start_position,
            cdc_start_time=cdc_start_time,
            id=id,
            replication_task_settings=replication_task_settings,
            start_replication_task=start_replication_task,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCdcStartPosition")
    def reset_cdc_start_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdcStartPosition", []))

    @jsii.member(jsii_name="resetCdcStartTime")
    def reset_cdc_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdcStartTime", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetReplicationTaskSettings")
    def reset_replication_task_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicationTaskSettings", []))

    @jsii.member(jsii_name="resetStartReplicationTask")
    def reset_start_replication_task(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartReplicationTask", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="replicationTaskArn")
    def replication_task_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationTaskArn"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="cdcStartPositionInput")
    def cdc_start_position_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdcStartPositionInput"))

    @builtins.property
    @jsii.member(jsii_name="cdcStartTimeInput")
    def cdc_start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdcStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="migrationTypeInput")
    def migration_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "migrationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationInstanceArnInput")
    def replication_instance_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationInstanceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationTaskIdInput")
    def replication_task_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationTaskIdInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationTaskSettingsInput")
    def replication_task_settings_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationTaskSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceEndpointArnInput")
    def source_endpoint_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceEndpointArnInput"))

    @builtins.property
    @jsii.member(jsii_name="startReplicationTaskInput")
    def start_replication_task_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "startReplicationTaskInput"))

    @builtins.property
    @jsii.member(jsii_name="tableMappingsInput")
    def table_mappings_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableMappingsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="targetEndpointArnInput")
    def target_endpoint_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetEndpointArnInput"))

    @builtins.property
    @jsii.member(jsii_name="cdcStartPosition")
    def cdc_start_position(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdcStartPosition"))

    @cdc_start_position.setter
    def cdc_start_position(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationTask, "cdc_start_position").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcStartPosition", value)

    @builtins.property
    @jsii.member(jsii_name="cdcStartTime")
    def cdc_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdcStartTime"))

    @cdc_start_time.setter
    def cdc_start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationTask, "cdc_start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationTask, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="migrationType")
    def migration_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "migrationType"))

    @migration_type.setter
    def migration_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationTask, "migration_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "migrationType", value)

    @builtins.property
    @jsii.member(jsii_name="replicationInstanceArn")
    def replication_instance_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationInstanceArn"))

    @replication_instance_arn.setter
    def replication_instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationTask, "replication_instance_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationInstanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="replicationTaskId")
    def replication_task_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationTaskId"))

    @replication_task_id.setter
    def replication_task_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationTask, "replication_task_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationTaskId", value)

    @builtins.property
    @jsii.member(jsii_name="replicationTaskSettings")
    def replication_task_settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationTaskSettings"))

    @replication_task_settings.setter
    def replication_task_settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationTask, "replication_task_settings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationTaskSettings", value)

    @builtins.property
    @jsii.member(jsii_name="sourceEndpointArn")
    def source_endpoint_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceEndpointArn"))

    @source_endpoint_arn.setter
    def source_endpoint_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationTask, "source_endpoint_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceEndpointArn", value)

    @builtins.property
    @jsii.member(jsii_name="startReplicationTask")
    def start_replication_task(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "startReplicationTask"))

    @start_replication_task.setter
    def start_replication_task(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationTask, "start_replication_task").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startReplicationTask", value)

    @builtins.property
    @jsii.member(jsii_name="tableMappings")
    def table_mappings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableMappings"))

    @table_mappings.setter
    def table_mappings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationTask, "table_mappings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableMappings", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationTask, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationTask, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="targetEndpointArn")
    def target_endpoint_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetEndpointArn"))

    @target_endpoint_arn.setter
    def target_endpoint_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DmsReplicationTask, "target_endpoint_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetEndpointArn", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dms.DmsReplicationTaskConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "migration_type": "migrationType",
        "replication_instance_arn": "replicationInstanceArn",
        "replication_task_id": "replicationTaskId",
        "source_endpoint_arn": "sourceEndpointArn",
        "table_mappings": "tableMappings",
        "target_endpoint_arn": "targetEndpointArn",
        "cdc_start_position": "cdcStartPosition",
        "cdc_start_time": "cdcStartTime",
        "id": "id",
        "replication_task_settings": "replicationTaskSettings",
        "start_replication_task": "startReplicationTask",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class DmsReplicationTaskConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        migration_type: builtins.str,
        replication_instance_arn: builtins.str,
        replication_task_id: builtins.str,
        source_endpoint_arn: builtins.str,
        table_mappings: builtins.str,
        target_endpoint_arn: builtins.str,
        cdc_start_position: typing.Optional[builtins.str] = None,
        cdc_start_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        replication_task_settings: typing.Optional[builtins.str] = None,
        start_replication_task: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS Database Migration Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param migration_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#migration_type DmsReplicationTask#migration_type}.
        :param replication_instance_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_instance_arn DmsReplicationTask#replication_instance_arn}.
        :param replication_task_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_task_id DmsReplicationTask#replication_task_id}.
        :param source_endpoint_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#source_endpoint_arn DmsReplicationTask#source_endpoint_arn}.
        :param table_mappings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#table_mappings DmsReplicationTask#table_mappings}.
        :param target_endpoint_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#target_endpoint_arn DmsReplicationTask#target_endpoint_arn}.
        :param cdc_start_position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#cdc_start_position DmsReplicationTask#cdc_start_position}.
        :param cdc_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#cdc_start_time DmsReplicationTask#cdc_start_time}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#id DmsReplicationTask#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param replication_task_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_task_settings DmsReplicationTask#replication_task_settings}.
        :param start_replication_task: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#start_replication_task DmsReplicationTask#start_replication_task}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#tags DmsReplicationTask#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#tags_all DmsReplicationTask#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DmsReplicationTaskConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument migration_type", value=migration_type, expected_type=type_hints["migration_type"])
            check_type(argname="argument replication_instance_arn", value=replication_instance_arn, expected_type=type_hints["replication_instance_arn"])
            check_type(argname="argument replication_task_id", value=replication_task_id, expected_type=type_hints["replication_task_id"])
            check_type(argname="argument source_endpoint_arn", value=source_endpoint_arn, expected_type=type_hints["source_endpoint_arn"])
            check_type(argname="argument table_mappings", value=table_mappings, expected_type=type_hints["table_mappings"])
            check_type(argname="argument target_endpoint_arn", value=target_endpoint_arn, expected_type=type_hints["target_endpoint_arn"])
            check_type(argname="argument cdc_start_position", value=cdc_start_position, expected_type=type_hints["cdc_start_position"])
            check_type(argname="argument cdc_start_time", value=cdc_start_time, expected_type=type_hints["cdc_start_time"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument replication_task_settings", value=replication_task_settings, expected_type=type_hints["replication_task_settings"])
            check_type(argname="argument start_replication_task", value=start_replication_task, expected_type=type_hints["start_replication_task"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "migration_type": migration_type,
            "replication_instance_arn": replication_instance_arn,
            "replication_task_id": replication_task_id,
            "source_endpoint_arn": source_endpoint_arn,
            "table_mappings": table_mappings,
            "target_endpoint_arn": target_endpoint_arn,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if cdc_start_position is not None:
            self._values["cdc_start_position"] = cdc_start_position
        if cdc_start_time is not None:
            self._values["cdc_start_time"] = cdc_start_time
        if id is not None:
            self._values["id"] = id
        if replication_task_settings is not None:
            self._values["replication_task_settings"] = replication_task_settings
        if start_replication_task is not None:
            self._values["start_replication_task"] = start_replication_task
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def migration_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#migration_type DmsReplicationTask#migration_type}.'''
        result = self._values.get("migration_type")
        assert result is not None, "Required property 'migration_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replication_instance_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_instance_arn DmsReplicationTask#replication_instance_arn}.'''
        result = self._values.get("replication_instance_arn")
        assert result is not None, "Required property 'replication_instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replication_task_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_task_id DmsReplicationTask#replication_task_id}.'''
        result = self._values.get("replication_task_id")
        assert result is not None, "Required property 'replication_task_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_endpoint_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#source_endpoint_arn DmsReplicationTask#source_endpoint_arn}.'''
        result = self._values.get("source_endpoint_arn")
        assert result is not None, "Required property 'source_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_mappings(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#table_mappings DmsReplicationTask#table_mappings}.'''
        result = self._values.get("table_mappings")
        assert result is not None, "Required property 'table_mappings' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_endpoint_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#target_endpoint_arn DmsReplicationTask#target_endpoint_arn}.'''
        result = self._values.get("target_endpoint_arn")
        assert result is not None, "Required property 'target_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cdc_start_position(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#cdc_start_position DmsReplicationTask#cdc_start_position}.'''
        result = self._values.get("cdc_start_position")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cdc_start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#cdc_start_time DmsReplicationTask#cdc_start_time}.'''
        result = self._values.get("cdc_start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#id DmsReplicationTask#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_task_settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_task_settings DmsReplicationTask#replication_task_settings}.'''
        result = self._values.get("replication_task_settings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_replication_task(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#start_replication_task DmsReplicationTask#start_replication_task}.'''
        result = self._values.get("start_replication_task")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#tags DmsReplicationTask#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#tags_all DmsReplicationTask#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsReplicationTaskConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DmsCertificate",
    "DmsCertificateConfig",
    "DmsEndpoint",
    "DmsEndpointConfig",
    "DmsEndpointElasticsearchSettings",
    "DmsEndpointElasticsearchSettingsOutputReference",
    "DmsEndpointKafkaSettings",
    "DmsEndpointKafkaSettingsOutputReference",
    "DmsEndpointKinesisSettings",
    "DmsEndpointKinesisSettingsOutputReference",
    "DmsEndpointMongodbSettings",
    "DmsEndpointMongodbSettingsOutputReference",
    "DmsEndpointRedshiftSettings",
    "DmsEndpointRedshiftSettingsOutputReference",
    "DmsEndpointS3Settings",
    "DmsEndpointS3SettingsOutputReference",
    "DmsEndpointTimeouts",
    "DmsEndpointTimeoutsOutputReference",
    "DmsEventSubscription",
    "DmsEventSubscriptionConfig",
    "DmsEventSubscriptionTimeouts",
    "DmsEventSubscriptionTimeoutsOutputReference",
    "DmsReplicationInstance",
    "DmsReplicationInstanceConfig",
    "DmsReplicationInstanceTimeouts",
    "DmsReplicationInstanceTimeoutsOutputReference",
    "DmsReplicationSubnetGroup",
    "DmsReplicationSubnetGroupConfig",
    "DmsReplicationTask",
    "DmsReplicationTaskConfig",
]

publication.publish()
