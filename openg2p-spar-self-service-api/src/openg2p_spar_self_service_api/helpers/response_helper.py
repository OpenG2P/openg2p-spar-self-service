from openg2p_fastapi_common.service import BaseService
from openg2p_mapper_interface_lib.interface import MapperResponse

from ..schemas import LinkResponse, ResponseStatus, LinkResponsePayload


class ResponseHelper(BaseService):

    def construct_link_response(self, mapper_response: MapperResponse) -> LinkResponse:
        return LinkResponse(
            response_status=(
                ResponseStatus.SUCCESS
                if mapper_response.status == "succ"
                else ResponseStatus.FAILURE
            ),
            response_payload=LinkResponsePayload(
                id=mapper_response.id,
                fa=mapper_response.fa,
                name=mapper_response.name,
                phone_number=mapper_response.phone_number,
                additional_info=mapper_response.additional_info,
            ),
            response_message=(
                mapper_response.mapper_error_message
                if mapper_response.mapper_error_message
                else None
            ),
        )
